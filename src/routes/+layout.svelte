<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="h-screen overflow-hidden bg-gray-50 text-gray-950 dark:bg-gray-950 dark:text-gray-50">
	{@render children()}
</div>
