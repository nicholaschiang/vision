<script lang="ts">
  import "../app.css"
  import { cn } from "$lib/cn"
  import { page } from "$app/state"
  import DarkModeSwitch from "./DarkModeSwitch.svelte"
  let { children } = $props()
</script>

{#snippet link(href: string, label: string)}
  <a
    {href}
    class={cn(
      "px-0.5 py-1 text-gray-400 transition hover:text-inherit dark:text-gray-600",
      page.url.pathname.includes(href) &&
        "text-inherit underline dark:text-inherit",
    )}>{label}</a
  >
{/snippet}

<div class="mx-auto flex items-start min-h-screen max-w-screen-lg">
  <nav class="sticky top-0 flex w-40 flex-none flex-col items-start py-2">
    {@render link("/posts", "Inspiration")}
    {@render link("/calendar", "Calendar")}
    {@render link("/wishlist", "Wishlist")}
    <DarkModeSwitch />
  </nav>
  {@render children()}
</div>
