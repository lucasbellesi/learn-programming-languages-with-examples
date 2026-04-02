// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: practicing performance and profiling basics patterns makes exercises and checkpoints easier to reason about.

import { performance } from "node:perf_hooks";

// Helper setup for performance and profiling basics; this keeps the walkthrough readable.
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

// Walk through one fixed scenario so performance and profiling basics behavior stays repeatable.
function main(): void {
    // Prepare sample inputs that exercise the key performance and profiling basics path.
    const values = Array.from({ length: 8_000 }, (_, index) => `item-${index}`);
    const runs = 12;

    const concatAverage = averageDuration(runs, () => {
        void buildWithConcat(values).length;
    });
    const joinAverage = averageDuration(runs, () => {
        void buildWithJoin(values).length;
    });

    // Report values so learners can verify the performance and profiling basics outcome.
    console.log(
        `Concat average (ms): ${concatAverage.toFixed(3)} over ${runs} runs`,
    );
    console.log(
        `Join average (ms): ${joinAverage.toFixed(3)} over ${runs} runs`,
    );
}

main();
