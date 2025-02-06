import click
import logging
import json
import os

from typing import List, Tuple
from instagrapi import Client
from instagrapi.exceptions import LoginRequired

logger = logging.getLogger()


def get_collections(cl: Client) -> List[dict]:
    """
    Get collections

    Returns
    -------
    List[Collection]
        A list of objects of Collection
    """
    next_max_id = ""
    total_items: List[dict] = []
    while True:
        try:
            result = cl.private_request(
                "collections/list/",
                params={
                    "collection_types": '["ALL_MEDIA_AUTO_COLLECTION","PRODUCT_AUTO_COLLECTION","MEDIA"]',
                    "max_id": next_max_id,
                },
            )
        except Exception as e:
            logger.exception(e)
            return total_items
        for item in result["items"]:
            total_items.append(item)
        if not result.get("more_available"):
            return total_items
        next_max_id = result.get("next_max_id", "")
    return total_items


def get_collection_medias(
    cl: Client, collection_pk: str, amount: int = 21, last_media_pk: int = 0
) -> List[dict]:
    """
    Get media in a collection by collection_pk

    Parameters
    ----------
    collection_pk: str
        Unique identifier of a Collection
    amount: int, optional
        Maximum number of media to return, default is 21
    last_media_pk: int, optional
        Last PK user has seen, function will return medias after this pk. Default is 0

    Returns
    -------
    List[Media]
        A list of objects of Media
    """
    last_media_pk = last_media_pk and int(last_media_pk)
    total_items = []
    next_max_id = ""
    amount = int(amount)
    found_last_media_pk = False
    while True:
        items, next_max_id = get_collection_medias_chunk(
            cl, collection_pk, max_id=next_max_id
        )
        for item in items:
            if last_media_pk and last_media_pk == item["pk"]:
                found_last_media_pk = True
                break
            total_items.append(item)
        if (amount and len(total_items) >= amount) or found_last_media_pk:
            break
        if not items or not next_max_id:
            break
    return total_items[:amount] if amount else total_items


def get_collection_medias_chunk(
    cl: Client, collection_pk: str, max_id: str = ""
) -> Tuple[List[dict], str]:
    """
    Get media in a collection by collection_pk

    Parameters
    ----------
    collection_pk: str
        Unique identifier of a Collection
    max_id: str, optional
        Cursor

    Returns
    -------
    Tuple[List[Media], str]
        A list of objects of Media and cursor
    """
    if isinstance(collection_pk, int) or collection_pk.isdigit():
        private_request_endpoint = f"feed/collection/{collection_pk}/"
    elif collection_pk.lower() == "liked":
        private_request_endpoint = "feed/liked/"
    else:
        private_request_endpoint = "feed/saved/posts/"

    params = {"include_igtv_preview": "false"}
    if max_id:
        params["max_id"] = max_id
    result = cl.private_request(private_request_endpoint, params=params)
    items = [m.get("media", m) for m in result["items"]]
    return items, result.get("next_max_id", "")


@click.command()
@click.option("--username", prompt="Your Instagram username")
@click.option("--password", prompt="Your Instagram password", hide_input=True)
@click.option("--session-file", default="data/session.json")
@click.option("--collections-file", default="data/collections.json")
@click.option("--media-file", default="data/media.json")
def main(
    username: str,
    password: str,
    session_file: str,
    collections_file: str,
    media_file: str,
) -> None:
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password. Then, proceeds to save collection
    information to the specified output file.
    """

    cl = Client()
    session = cl.load_settings(session_file) if os.path.exists(session_file) else None

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(username, password)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                logger.info("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(username, password)
            login_via_session = True
        except Exception as e:
            logger.info("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            logger.info("Attempting to login via username and password. username: %s" % username)
            if cl.login(username, password):
                login_via_pw = True
        except Exception as e:
            logger.info("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")

    if not os.path.exists(collections_file):
        logger.info("Getting collections")
        collections = get_collections(cl)
        with open(collections_file, "w") as f:
            json.dump(collections, f)
    else:
        logger.info("Reading collections from file")
        with open(collections_file, "r") as f:
            collections = json.load(f)

    collection = collections[0]
    logger.info("Getting media from collection: %s", collection["collection_name"])
    media = get_collection_medias(cl, collection_pk=collection["collection_id"], amount=1000)
    with open(media_file, "w") as f:
        json.dump(media, f)

    cl.dump_settings(session_file)


if __name__ == "__main__":
    main()
