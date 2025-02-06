<script lang="ts">
	import posts from '../posts.json';
	import collections from '../collections.json';

	let selectedCollectionIds = $state([collections[0].collection_id]);
	let filteredPosts = $derived(posts.filter((post) => post.saved_collection_ids.some((collectionId) => selectedCollectionIds.includes(collectionId))));
</script>

<div class="flex flex-col gap-2 py-2">
	<div class="filter-group">
		{#each collections as collection (collection.collection_id)}
			<button
				class="filter"
				data-state={selectedCollectionIds.includes(collection.collection_id) ? 'selected' : null}
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
			</button>
		{/each}
	</div>
	<div class="grid grid-cols-4 gap-2 px-2">
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
</div>

<style>
	:root {
		--mono3: #232323;
		--mono4: #282828;
		--mono5: #1a1a1a;
		--mono8: #505050;
		--mono11: #a0a0a0;
		--mono12: #ededed;
	}
	.filter-group,
	.filter {
		display: flex;
		align-items: center;
	}
	.filter-group {
		flex-wrap: wrap;
		row-gap: 8px;
	}
	.filter {
		--height: 36px;
		z-index: 1;
		-webkit-user-select: none;
		-moz-user-select: none;
		user-select: none;
		cursor: pointer;
		height: var(--height);
		border-radius: var(--height);
		padding: 0 16px;
		border: 1px solid var(--mono5);
		justify-content: center;
		color: var(--mono11);
		text-wrap: nowrap;
		font-size: 14px;
		transition: 100ms;
		transition-property: margin, padding, border-color, border-radius, background, color;
	}
	.filter {
		z-index: 0;
		margin-left: 8px;
	}
	.filter[data-state='selected'] {
		z-index: 1;
		background: var(--mono4);
		border-color: var(--mono8);
		color: var(--mono12);
	}
	.filter[data-state='selected'] + .filter[data-state='selected'] {
		z-index: 0;
		margin-left: -16px;
		padding-left: 28px;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		border-left-color: transparent;
		background: var(--mono3);
	}
</style>
