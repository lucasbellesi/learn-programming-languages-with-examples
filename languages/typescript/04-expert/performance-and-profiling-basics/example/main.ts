// This example shows measuring hot paths before changing code for speed.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

import { performance } from "node:perf_hooks";

// Define the reusable pieces first so the main flow can focus on one observable scenario.
function buildWithConcat(values: string[]): string {
    let output = "";
    for (const value of values) {
        output += `${value},`;
    }
    return output;
}

function buildWithJoin(values: string[]): string {
    return values.join(",");
}

function averageDuration(runs: number, work: () => void): number {
    work();
    const start = performance.now();
    for (let index = 0; index < runs; index += 1) {
        work();
    }
    return (performance.now() - start) / runs;
}

// Run one deterministic scenario so the console output makes measuring hot paths before changing code for speed easy to verify.
function main(): void {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const values = Array.from({ length: 8_000 }, (_, index) => `item-${index}`);
    const runs = 12;

    const concatAverage = averageDuration(runs, () => {
        void buildWithConcat(values).length;
    });
    const joinAverage = averageDuration(runs, () => {
        void buildWithJoin(values).length;
    });

    // Print the observed state here so learners can connect the code path to a concrete result.
    console.log(
        `Concat average (ms): ${concatAverage.toFixed(3)} over ${runs} runs`,
    );
    console.log(
        `Join average (ms): ${joinAverage.toFixed(3)} over ${runs} runs`,
    );
}

main();
