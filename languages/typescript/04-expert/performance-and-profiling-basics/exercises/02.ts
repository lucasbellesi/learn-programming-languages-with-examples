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
    const values = Array.from({ length: 5_000 }, (_, index) => `row-${index}`);
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

    console.log(`Concat average (ms): ${concatAverage.toFixed(3)}`);
    console.log(`Buffered average (ms): ${bufferedAverage.toFixed(3)}`);
}

main();

export {};
