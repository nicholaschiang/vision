<script lang="ts">
  import posts from "../posts.json"
  import collections from "../collections.json"

  import Button from "$lib/components/Button.svelte"
  import Media from "$lib/components/Media.svelte"
  import VirtualList from "$lib/components/VirtualList.svelte"

  import { Plus, Minus, Fullscreen } from "lucide-svelte"

  let gridCols = $state(3)
  let selectedCollectionIds = $state(["18031828522742161"])
  let filteredPosts = $derived.by(() => {
    const arr = posts.filter(
      (post) =>
        selectedCollectionIds.includes("ALL_MEDIA_AUTO_COLLECTION") ||
        selectedCollectionIds.every((collectionId) =>
          (post.saved_collection_ids as string[]).includes(collectionId),
        ),
    )
    const arrs = []
    while (arr.length) arrs.push(arr.splice(0, gridCols))
    return arrs
  })
</script>

<div class="flex w-0 grow flex-col gap-2">
  <div class="flex flex-none gap-2 overflow-x-auto">
    <Button
      data-active
      class="flex aspect-square items-center justify-center p-0"
      onclick={() => {
        if (document.fullscreenElement) {
          document
            .exitFullscreen()
            .then(() => console.log("Document Exited from Full screen mode"))
            .catch((err) => console.error(err))
        } else {
          document.documentElement.requestFullscreen()
        }
      }}
    >
      <Fullscreen class="h-4 w-4" />
    </Button>
    <Button
      data-active
      class="flex aspect-square items-center justify-center p-0"
      onclick={() => {
        gridCols--
      }}
    >
      <Plus class="h-4 w-4" />
    </Button>
    <Button
      data-active
      class="flex aspect-square items-center justify-center p-0"
      onclick={() => {
        gridCols++
      }}
    >
      <Minus class="h-4 w-4" />
    </Button>
    {#each collections as collection (collection.collection_id)}
      <Button
        class="whitespace-nowrap"
        data-active={selectedCollectionIds.includes(collection.collection_id)
          ? ""
          : undefined}
        onclick={() => {
          if (selectedCollectionIds.includes(collection.collection_id)) {
            selectedCollectionIds = selectedCollectionIds.filter(
              (id) => id !== collection.collection_id,
            )
          } else {
            selectedCollectionIds = [
              ...selectedCollectionIds,
              collection.collection_id,
            ]
          }
        }}
      >
        {collection.collection_name}
      </Button>
    {/each}
  </div>
  <div class="h-0 grow">
    <VirtualList items={filteredPosts} height="100%">
      {#snippet children(item)}
        <div
          class="mb-2 grid gap-2"
          style:grid-template-columns={`repeat(${gridCols}, minmax(0, 1fr))`}
        >
          {#each item as post (post.id)}
            {#if post.carousel_media}
              <div
                class="flex aspect-9/16 snap-x snap-mandatory overflow-x-auto overflow-y-hidden rounded"
              >
                {#each post.carousel_media as media, index (media.id)}
                  <a
                    aria-label={post.caption?.text}
                    href={`https://instagram.com/p/${post.code}?img_index=${index + 1}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="aspect-9/16 min-w-full snap-start"
                  >
                    <Media {media} />
                  </a>
                {/each}
              </div>
            {:else}
              <a
                aria-label={post.caption?.text}
                href={`https://instagram.com/p/${post.code}`}
                target="_blank"
                rel="noopener noreferrer"
                class="aspect-9/16 overflow-hidden rounded"
              >
                <Media media={post} />
              </a>
            {/if}
          {/each}
        </div>
      {/snippet}
    </VirtualList>
  </div>
</div>
