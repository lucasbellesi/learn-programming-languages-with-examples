// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: the example makes it possible to measure before optimizing and interpret timing
// data cautiously before the learner tackles the exercises.

import { performance } from "node:perf_hooks";

// Separate helpers keep the main path focused on how to measure before optimizing and interpret
// timing data cautiously.
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

// Fixed inputs make the consequence of measuring tiny workloads where noise dominates the result
// visible and repeatable.
function main(): void {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const values = Array.from({ length: 8_000 }, (_, index) => `item-${index}`);
    const runs = 12;

    const concatAverage = averageDuration(runs, () => {
        void buildWithConcat(values).length;
    });
    const joinAverage = averageDuration(runs, () => {
        void buildWithJoin(values).length;
    });

    // The printed result shows whether the program can relate algorithmic and allocation choices
    // to observed cost.
    console.log(
        `Concat average (ms): ${concatAverage.toFixed(3)} over ${runs} runs`,
    );
    console.log(
        `Join average (ms): ${joinAverage.toFixed(3)} over ${runs} runs`,
    );
}

main();
