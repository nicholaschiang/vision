import { error } from "@sveltejs/kit"

import posts from "$lib/data/posts.json"
import post from "$lib/data/post.json"

type Post = typeof post

export async function load({ params }) {
  const post = (posts as Post[]).find((post) => post.id === params.postId)
  console.log(params.postId)
  console.log(post)
  if (post == null) error(404, { message: "Post not found" })
  return post
}
