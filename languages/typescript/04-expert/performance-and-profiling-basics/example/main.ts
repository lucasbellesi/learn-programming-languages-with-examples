import { performance } from "node:perf_hooks";

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

function main(): void {
    const values = Array.from({ length: 8_000 }, (_, index) => `item-${index}`);
    const runs = 12;

    const concatAverage = averageDuration(runs, () => {
        void buildWithConcat(values).length;
    });
    const joinAverage = averageDuration(runs, () => {
        void buildWithJoin(values).length;
    });

    console.log(
        `Concat average (ms): ${concatAverage.toFixed(3)} over ${runs} runs`,
    );
    console.log(
        `Join average (ms): ${joinAverage.toFixed(3)} over ${runs} runs`,
    );
}

main();
