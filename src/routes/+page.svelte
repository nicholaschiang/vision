<script lang="ts">
	import posts from '../posts.json';
	import collections from '../collections.json';

	import Button from '$lib/components/Button.svelte';
	import Media from '$lib/components/Media.svelte';
	import VirtualList from '$lib/components/VirtualList.svelte';

	import { Plus, Minus } from 'lucide-svelte';

	let gridCols = $state(4);
	let selectedCollectionIds = $state([collections[0].collection_id]);
	let filteredPosts = $derived.by(() => {
		const arr = posts.filter(
			(post) =>
				selectedCollectionIds.includes('ALL_MEDIA_AUTO_COLLECTION') ||
				selectedCollectionIds.every((collectionId) =>
					(post.saved_collection_ids as string[]).includes(collectionId)
				)
		);
		const arrs = [];
		while (arr.length) arrs.push(arr.splice(0, gridCols));
		return arrs;
	});
</script>

<div class="flex h-screen flex-col overflow-hidden">
	<div class="flex flex-none flex-wrap gap-2 p-2">
		{#each collections as collection (collection.collection_id)}
			<Button
				data-active={selectedCollectionIds.includes(collection.collection_id) ? '' : undefined}
				onclick={() => {
					if (selectedCollectionIds.includes(collection.collection_id)) {
						selectedCollectionIds = selectedCollectionIds.filter(
							(id) => id !== collection.collection_id
						);
					} else {
						selectedCollectionIds = [...selectedCollectionIds, collection.collection_id];
					}
				}}
			>
				{collection.collection_name}
			</Button>
		{/each}
	</div>

	<div class="flex flex-none gap-2 px-2 pt-1 pb-3">
		<Button
			class="flex h-6 w-6 items-center justify-center rounded-full p-0"
			onclick={() => {
				gridCols--;
			}}
		>
			<Plus class="h-4 w-4" />
		</Button>
		<Button
			class="flex h-6 w-6 items-center justify-center rounded-full p-0"
			onclick={() => {
				gridCols++;
			}}
		>
			<Minus class="h-4 w-4" />
		</Button>
	</div>

	<div class="h-0 grow">
		<VirtualList items={filteredPosts} height="100%">
			{#snippet children(item)}
				<div
					class="grid gap-2 px-2 py-1"
					style:grid-template-columns={`repeat(${gridCols}, minmax(0, 1fr))`}
				>
					{#each item as post (post.id)}
						{#if post.carousel_media}
							<div class="flex aspect-4/5 snap-x snap-mandatory overflow-x-auto overflow-y-hidden">
								{#each post.carousel_media as media, index (media.id)}
									<a
										aria-label={post.caption?.text}
										href={`https://instagram.com/p/${post.code}?img_index=${index + 1}`}
										target="_blank"
										rel="noopener noreferrer"
										class="aspect-4/5 w-full snap-start"
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
								class="aspect-4/5"
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
