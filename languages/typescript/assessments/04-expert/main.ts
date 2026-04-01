import { setTimeout as delay } from "node:timers/promises";

type WorkerSummary = {
    workerId: number;
    total: number;
    minimum: number;
    maximum: number;
};

async function processChunk(
    workerId: number,
    values: number[],
): Promise<WorkerSummary> {
    await delay((workerId + 1) * 5);

    let total = 0;
    let minimum = values[0] ?? 0;
    let maximum = values[0] ?? 0;

    for (const value of values) {
        total += value;
        minimum = Math.min(minimum, value);
        maximum = Math.max(maximum, value);
    }

    return {
        workerId,
        total,
        minimum,
        maximum,
    };
}

async function main(): Promise<void> {
    const data = [12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6];
    const workerCount = 3;
    const chunkSize = Math.ceil(data.length / workerCount);

    const jobs: Promise<WorkerSummary>[] = [];
    for (let workerId = 0; workerId < workerCount; workerId += 1) {
        const begin = workerId * chunkSize;
        const end = Math.min(begin + chunkSize, data.length);
        jobs.push(processChunk(workerId, data.slice(begin, end)));
    }

    const summaries = await Promise.all(jobs);

    for (const summary of summaries) {
        console.log(`Worker ${summary.workerId} partial sum: ${summary.total}`);
    }

    const total = summaries.reduce((sum, summary) => sum + summary.total, 0);
    const minimum = summaries.reduce(
        (best, summary) => Math.min(best, summary.minimum),
        Number.POSITIVE_INFINITY,
    );
    const maximum = summaries.reduce(
        (best, summary) => Math.max(best, summary.maximum),
        Number.NEGATIVE_INFINITY,
    );

    console.log("");
    console.log("Final summary:");
    console.log(`Total: ${total}`);
    console.log(`Minimum: ${minimum}`);
    console.log(`Maximum: ${maximum}`);
}

main().catch((error: unknown) => {
    if (error instanceof Error) {
        console.error(error.message);
    } else {
        console.error("Unknown error");
    }
    process.exitCode = 1;
});
