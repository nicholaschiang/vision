<script lang="ts">
  import Media from "$lib/components/Media.svelte"
  import Habit from "$lib/components/Habit.svelte"
  import { Plus } from "lucide-svelte"
  let { data: post } = $props()
</script>

{#snippet header(title: string, subtitle: string)}
  <header>
    <h1>{title}</h1>
    <p class="text-xs text-gray-400 dark:text-gray-600">{subtitle}</p>
  </header>
{/snippet}

{#snippet product()}
  <div class="grid gap-1">
    <img
      src="https://dtcralphlauren.scene7.com/is/image/PoloGSI/s7-1224539_lifestyle?$rl_4x5_pdp$"
      class="aspect-square w-full rounded"
      alt=""
    />
    <div class="flex items-start justify-between gap-2 text-xs">
      <p class="truncate">Leather Racer Jacket</p>
      <p class="text-gray-400 dark:text-gray-600">$300–700</p>
    </div>
  </div>
{/snippet}

<div class="grid grid-cols-2 gap-6 p-6">
  <div class="grid gap-4">
    {@render header("Post", "The inspiration. The vision to realize.")}
    <div class="flex items-center gap-2">
      <img
        src={`/media?url=${encodeURIComponent(post.user.profile_pic_url)}`}
        alt={post.user.username}
        class="h-10 w-10 rounded-full"
      />
      <div>
        <p class="text-sm font-medium">{post.user.username}</p>
        <p class="text-xs text-gray-400 dark:text-gray-600">
          {post.user.full_name}
        </p>
      </div>
    </div>
    <div class="grid gap-2">
      {#if post.carousel_media}
        {#each post.carousel_media as media (media.id)}
          <Media class="h-auto w-full rounded" {media} />
        {/each}
      {:else}
        <Media class="h-auto w-full rounded" media={post} />
      {/if}
    </div>
  </div>
  <div class="flex flex-col gap-8">
    <div class="grid gap-4">
      {@render header(
        "Products",
        "Purchasable products shown in this post (e.g. clothing, food, cars).",
      )}
      <div class="grid grid-cols-2 gap-2">
        {@render product()}
        {@render product()}
        {@render product()}
        <button
          class="flex aspect-square w-full items-center justify-center border border-dashed border-gray-200 dark:border-gray-800"
        >
          <Plus class="h-4 w-4" />
        </button>
      </div>
    </div>
    <div class="grid gap-4">
      {@render header(
        "Habits",
        "Tasks that, when completed regularly, will lead to what is pictured in this post (e.g. gym, running, completing HW, eating certain calories).",
      )}
      <Habit />
      <Habit />
      <Habit />
    </div>
    <div>
      {@render header(
        "Calendar events",
        "Milestones related to this post (e.g. concerts, large purchases, travel).",
      )}
    </div>
  </div>
</div>
