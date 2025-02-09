<script lang="ts">
  import { cn } from "$lib/cn"

  type Media = {
    video_versions?: { url: string }[]
    image_versions2?: { candidates?: { url: string }[] }
    caption?: { text: string } | null
  }
  let { media, ...props }: { media: Media; class?: string } = $props()
  let image = $derived(media.image_versions2?.candidates?.[0].url)
  let video = $derived(media.video_versions?.[0].url)
</script>

{#if video}
  <video
    src={`/media?url=${encodeURIComponent(video)}`}
    poster={image ? `/media?url=${encodeURIComponent(image)}` : undefined}
    class={cn("h-full w-full object-cover", props.class)}
    preload="none"
    loop
    onmouseover={(event) => event.currentTarget.play()}
    onfocus={(event) => event.currentTarget.play()}
    onmouseout={(event) => event.currentTarget.pause()}
    onblur={(event) => event.currentTarget.pause()}
  >
    <track kind="captions" />
  </video>
{:else if image}
  <img
    src={`/media?url=${encodeURIComponent(image)}`}
    alt={media.caption?.text}
    class={cn("h-full w-full object-cover", props.class)}
    loading="lazy"
    decoding="async"
  />
{:else}
  <div
    class={cn(
      "flex h-full w-full items-center justify-center border border-dashed border-gray-300 p-2 dark:border-gray-700",
      props.class,
    )}
  >
    <p class="text-xs text-gray-300 dark:text-gray-700">No media found</p>
  </div>
{/if}
