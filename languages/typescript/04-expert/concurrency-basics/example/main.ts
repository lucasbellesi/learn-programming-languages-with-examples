// This example shows starting multiple units of work and combining their results safely.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

import { setTimeout as delay } from "node:timers/promises";

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

// Run one deterministic scenario so the console output makes starting multiple units of work and combining their results safely easy to verify.
async function main(): Promise<void> {
    // Promise.all keeps the output order tied to the request order.
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const results = await Promise.all([
        loadJob("load", 25, 3),
        loadJob("validate", 10, 5),
        loadJob("save", 15, 4),
    ]);

    const total = results.reduce((sum, result) => sum + result.score, 0);

    // Print the observed state here so learners can connect the code path to a concrete result.
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
