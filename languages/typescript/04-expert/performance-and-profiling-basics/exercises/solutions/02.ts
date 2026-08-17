import { readFileSync } from "node:fs";
import { performance } from "node:perf_hooks";

function averageDuration(runs: number, work: () => void): number {
    work();
    const start = performance.now();
    for (let index = 0; index < runs; index += 1) {
        work();
    }
    return (performance.now() - start) / runs;
}

function main(): void {
    const requestedSize = Number(readFileSync(0, "utf8").trim());
    const size =
        Number.isInteger(requestedSize) && requestedSize >= 0
            ? requestedSize
            : 0;
    const values = Array.from({ length: size }, (_, index) => `row-${index}`);
    const runs = 12;

    const concatAverage = averageDuration(runs, () => {
        let output = "";
        for (const value of values) {
            output += value;
        }
        void output.length;
    });
    const bufferedAverage = averageDuration(runs, () => {
        const parts: string[] = [];
        for (const value of values) {
            parts.push(value);
        }
        void parts.join("").length;
    });

    console.log(`Values: ${size}`);
    console.log(`Concat average (ms): ${concatAverage.toFixed(3)}`);
    console.log(`Buffered average (ms): ${bufferedAverage.toFixed(3)}`);
}

main();

export {};
