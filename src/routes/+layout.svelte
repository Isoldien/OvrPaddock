<script lang="ts">
	let { children } = $props();
	import "../app.css";
</script>

<main class="bg-black">
	{@render children()}
</main>
