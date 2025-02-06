<script lang="ts">
	type Media = {
		video_versions?: { url: string }[];
		image_versions2?: { candidates?: { url: string }[] };
		caption?: { text: string } | null;
	};
	let { media }: { media: Media } = $props();
	let image = $derived(media.image_versions2?.candidates?.[0].url);
	let video = $derived(media.video_versions?.[0].url);
</script>

{#if video}
	<video
		src={`/media?url=${encodeURIComponent(video)}`}
		poster={image ? `/media?url=${encodeURIComponent(image)}` : undefined}
		class="h-full w-full object-cover"
		controls
		preload="none"
	>
		<track kind="captions" />
	</video>
{:else if image}
	<img
		src={`/media?url=${encodeURIComponent(image)}`}
		alt={media.caption?.text}
		class="h-full w-full object-cover"
		loading="lazy"
		decoding="async"
	/>
{:else}
	<div
		class="flex h-full w-full items-center justify-center border border-dashed border-gray-300 p-2 dark:border-gray-700"
	>
		<p class="text-sm text-gray-300 dark:text-gray-700">No media found</p>
	</div>
{/if}
