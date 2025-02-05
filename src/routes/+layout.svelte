<script lang="ts">
	import '../app.css';
	let { children } = $props();
</script>

<div class="bg-gray-950 text-gray-50 min-h-screen">
	{@render children()}
</div>
