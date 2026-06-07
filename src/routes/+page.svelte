<script lang="ts">


    let observer: IntersectionObserver;
    /* @TODO Add this to +layout.svelte for global scroll reveal */
    function reveal(node: HTMLElement) {
        if (typeof window !== "undefined" && !observer) {
            observer = new IntersectionObserver(
                (entries) => {
                    entries.forEach((entry) => {
                        if (entry.isIntersecting) {
                            entry.target.classList.remove(
                                "opacity-0",
                                "translate-y-10",
                            );
                            entry.target.classList.add(
                                "opacity-100",
                                "translate-y-0",
                            );
                        } else {
                            entry.target.classList.remove(
                                "opacity-100",
                                "translate-y-0",
                            );
                            entry.target.classList.add(
                                "opacity-0",
                                "translate-y-10",
                            );
                        }
                    });
                },
                { threshold: 0.2 },
            );
        }

        if (observer) observer.observe(node);

        return {
            destroy() {
                if (observer) observer.unobserve(node);
            },
        };
    }
</script>

<main
    class="relative bg-black flex flex-col items-center p-6 smooth-scroll select-none w-full overflow-hidden"
>
    <section
        class="min-h-screen flex flex-col items-center justify-center w-full"
    >
        <h1
            class="text-7xl font-tourney font-bold tracking-tight bg-linear-to-r from-gray-50 to-slate-600 bg-clip-text text-transparent"
        >
            OvrPaddock
        </h1>
        <h2 class="text-4xl font-spacemono text-gray-500 mt-4">
            ↓
        </h2>
    </section>

    <section
        use:reveal
        class="min-h-screen flex flex-col items-center justify-center w-full max-w-2xl text-center transition-all duration-1000 ease-out opacity-0 translate-y-10"
    >
        <div class="mb-6">
            <h2 class="text-4xl font-bold text-white mb-4 font-tourney">
                What is OvrPaddock?
            </h2>
        </div>
        <div>
            <p class="text-1xs font-spacemono text-white">
                OvrPaddock is a tool designed to allow users to watch replays or live races in a unique way, by providing a 3D environment where users can see a isometric view of the track and the cars.  
        </div>
        <div class="mt-6">
            <button
                class="mt-6 px-4 py-2 bg-black outline-1 text-white transition font-spacemono rounded-sm"
                onclick={() => (window.location.href = "/dashboard")}
                >Continue</button>
        </div>
    </section> 
</main>
