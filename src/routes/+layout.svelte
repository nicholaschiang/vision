<script lang="ts">
  import "../app.css"
  import { cn } from "$lib/cn"
  import { page } from "$app/state"
  let { children } = $props()
</script>

{#snippet link(href: string, label: string)}
  <a
    {href}
    class={cn(
      "px-0.5 py-1 text-gray-600 transition hover:text-inherit dark:text-gray-400",
      page.url.pathname === href && "text-inherit underline dark:text-inherit",
    )}>{label}</a
  >
{/snippet}

<div
  class="h-screen overflow-hidden bg-gray-50 text-gray-950 dark:bg-gray-950 dark:text-gray-50"
>
  <div class="mx-auto flex h-full max-w-screen-lg">
    <nav class="flex w-40 flex-none flex-col">
      {@render link("/", "Inspiration")}
      {@render link("/calendar", "Calendar")}
      {@render link("/wishlist", "Wishlist")}
      <button
        class="px-0.5 py-1 text-left text-gray-600 hover:text-inherit dark:text-gray-400"
        onclick={() => {
          if (document.documentElement.classList.contains("dark")) {
            document.documentElement.classList.remove("dark")
          } else {
            document.documentElement.classList.add("dark")
          }
        }}>Theme</button
      >
    </nav>
    {@render children()}
  </div>
</div>
