<script lang="ts">
	let { children } = $props();
	import "../app.css";
	import githubIcon from "$lib/assets/github.svg";
    import Footer from "$lib/components/Footer.svelte";
</script>


<main class="bg-black">
	<Footer />
	{@render children()}
</main>



