// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: the example makes it possible to coordinate concurrent work without data races
// or lost results before the learner tackles the exercises.

import { setTimeout as delay } from "node:timers/promises";

// Separate helpers keep the main path focused on how to coordinate concurrent work without data
// races or lost results.
type JobResult = {
    name: string;
    score: number;
};

async function loadJob(
    name: string,
    waitMs: number,
    score: number,
): Promise<JobResult> {
    await delay(waitMs);
    return { name, score };
}

// Fixed inputs make the consequence of confusing concurrency with parallel CPU work visible and
// repeatable.
async function main(): Promise<void> {
    // Promise.all keeps the output order tied to the request order.
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const results = await Promise.all([
        loadJob("load", 25, 3),
        loadJob("validate", 10, 5),
        loadJob("save", 15, 4),
    ]);

    const total = results.reduce((sum, result) => sum + result.score, 0);

    // The printed result shows whether the program can define completion, cancellation, and error
    // propagation behavior.
    console.log(`Completed ${results.length} concurrent jobs.`);
    for (const result of results) {
        console.log(`- ${result.name}: ${result.score}`);
    }
    console.log(`Total value: ${total}`);
}

main().catch((error: unknown) => {
    if (error instanceof Error) {
        console.error(error.message);
    } else {
        console.error("Unknown error");
    }
    process.exitCode = 1;
});
