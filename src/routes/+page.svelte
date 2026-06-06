<script lang="ts">
    import githubIcon from "$lib/assets/github.svg";

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
            class="text-7xl font-tourney font-bold tracking-tight bg-gradient-to-r from-gray-50 to-slate-600 bg-clip-text text-transparent"
        >
            OvrPaddock
        </h1>

        <div class="mt-4">
            <p class="text-1xs font-spacemono max-w-md text-center text-white">
                By <strong>Isoldien</strong>
            </p>
        </div>
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
            <p class="text-white text-lg leading-relaxed font-spacemono">
                OvrPaddock is all-in-one F1 tracker. The name comes from <em
                    >Ovr</em
                >
                from many sports games signifying their <em>Overall</em> rating
                and <em>Paddock</em> is essentially the heart of F1.
            </p>
            <br />
            <p class="text-white text-lg leading-relaxed font-spacemono">
                By combining the two, we have <strong>OvrPaddock</strong> which
                could mean Overall Paddock, meaning
                <strong>"in general"</strong>
                so general news about F1 or Over [the] Paddock which means a literal
                <strong>birdseye view</strong> of the track. <br /><br />
                Either one you choose, I hope that it provides the information you
                require.
            </p>
        </div>
    </section>

    <div
        class="fixed bottom-6 flex flex-col items-center w-full pointer-events-none"
    >
        <div class="pointer-events-auto">
            <a
                href="https://github.com/Isoldien/OvrPaddock"
                class="transition hover:opacity-75"
            >
                <img class="w-5" src={githubIcon} alt="Github Icon" />
            </a>
        </div>
    </div>
</main>
