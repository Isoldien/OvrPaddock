<script lang="ts">
    import { Canvas } from "@threlte/core";
    import Scene from "./_scene.svelte";
</script>

<main
    class="relative min-h-screen bg-black flex flex-col items-center justify-center p-6 smooth-scroll select-none"
>
    <h1
        class="text-7xl font-tourney font-bold tracking-tight text-white bg-clip-text text-transparent"
    >
        OvrPaddock
    </h1>

    <div class="">
        <p class="text-1xs font-spacemono max-w-md text-center text-white">
            By <strong>Isoldien</strong>
        </p>
    </div>

    <!--
    <div>
        <Canvas>
            <Scene />
        </Canvas>
    </div>
-->
    <div class="absolute bottom-6 flex flex-col items-center">
        <div>
            <a href="https://github.com/Isoldien/OvrPaddock">
                <img
                    class="w-5"
                    src="src/lib/assets/github.svg"
                    alt="Github Icon"
                />
            </a>
        </div>
    </div>
</main>
