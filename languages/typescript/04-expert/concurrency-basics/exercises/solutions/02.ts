import { setTimeout as delay } from "node:timers/promises";

async function runWithLimit<T>(
    values: T[],
    limit: number,
    worker: (value: T) => Promise<string>,
): Promise<string[]> {
    const results = new Array<string>(values.length);
    let nextIndex = 0;

    async function runWorker(): Promise<void> {
        while (nextIndex < values.length) {
            const currentIndex = nextIndex;
            nextIndex += 1;
            results[currentIndex] = await worker(values[currentIndex]!);
        }
    }

    const runners = Array.from({ length: Math.min(limit, values.length) }, () =>
        runWorker(),
    );
    await Promise.all(runners);
    return results;
}

async function main(): Promise<void> {
    const jobs = [30, 10, 20, 5];
    const results = await runWithLimit(jobs, 2, async (waitMs) => {
        await delay(waitMs);
        return `finished ${waitMs}`;
    });

    for (const result of results) {
        console.log(result);
    }
}

main().catch((error: unknown) => {
    if (error instanceof Error) {
        console.error(error.message);
    }
    process.exitCode = 1;
});
