<script lang="ts">
	import posts from '../posts.json';
	import collections from '../collections.json';

	import Button from '$lib/components/Button.svelte';

	import { Plus, Minus } from 'lucide-svelte';

	let gridCols = $state(4);
	let selectedCollectionIds = $state([collections[0].collection_id]);
	let filteredPosts = $derived(
		posts.filter(
			(post) =>
				selectedCollectionIds.includes('ALL_MEDIA_AUTO_COLLECTION') ||
				post.saved_collection_ids.some((collectionId) =>
					selectedCollectionIds.includes(collectionId)
				)
		)
	);
</script>

<div class="flex flex-wrap gap-2 p-2">
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

<div class="flex gap-2 p-2">
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

<div class="grid gap-2 p-2" style:grid-template-columns={`repeat(${gridCols}, minmax(0, 1fr))`}>
	{#each filteredPosts as post}
		<a
			aria-label={post.caption?.text}
			href={`https://instagram.com/p/${post.code}`}
			target="_blank"
			rel="noopener noreferrer"
			class="aspect-4/5"
		>
			<img
				src={`/media?url=${encodeURIComponent(post.image_versions2.candidates[0].url)}`}
				alt={post.caption?.text}
				class="h-full w-full object-cover"
			/>
		</a>
	{/each}
</div>
