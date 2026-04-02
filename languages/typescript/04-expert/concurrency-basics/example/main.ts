// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to reason about.

import { setTimeout as delay } from "node:timers/promises";

// Helper setup for concurrency basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so concurrency basics behavior stays repeatable.
async function main(): Promise<void> {
    // Promise.all keeps the output order tied to the request order.
    // Prepare sample inputs that exercise the key concurrency basics path.
    const results = await Promise.all([
        loadJob("load", 25, 3),
        loadJob("validate", 10, 5),
        loadJob("save", 15, 4),
    ]);

    const total = results.reduce((sum, result) => sum + result.score, 0);

    // Report values so learners can verify the concurrency basics outcome.
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
