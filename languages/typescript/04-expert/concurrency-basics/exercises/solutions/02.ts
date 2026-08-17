import { readFileSync } from "node:fs";
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
    const [limitLine = "1", ...jobLines] = readFileSync(0, "utf8")
        .trimEnd()
        .split(/\r?\n/);
    const limit = Number(limitLine);
    const jobs = jobLines
        .map((line) => line.trim())
        .filter((line) => line.length > 0)
        .map(Number);
    if (!Number.isInteger(limit) || limit <= 0) {
        console.log("Worker limit must be positive.");
        return;
    }
    if (jobs.length === 0) {
        console.log("No jobs.");
        return;
    }
    const results = await runWithLimit(jobs, limit, async (waitMs) => {
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
