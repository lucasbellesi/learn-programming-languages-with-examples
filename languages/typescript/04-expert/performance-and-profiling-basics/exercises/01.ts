import { performance } from "node:perf_hooks";

type Pair = {
    key: string;
    value: number;
};

function averageDuration(runs: number, work: () => void): number {
    work();
    const start = performance.now();
    for (let index = 0; index < runs; index += 1) {
        work();
    }
    return (performance.now() - start) / runs;
}

function main(): void {
    const records: Pair[] = Array.from({ length: 4_000 }, (_, index) => ({
        key: `key-${index}`,
        value: index,
    }));
    const lookupMap = new Map(
        records.map((record) => [record.key, record.value]),
    );
    const runs = 12;

    const scanAverage = averageDuration(runs, () => {
        for (const target of ["key-10", "key-2000", "key-3999"]) {
            void records.find((record) => record.key === target)?.value;
        }
    });
    const mapAverage = averageDuration(runs, () => {
        for (const target of ["key-10", "key-2000", "key-3999"]) {
            void lookupMap.get(target);
        }
    });

    console.log(`Scan average (ms): ${scanAverage.toFixed(3)}`);
    console.log(`Map average (ms): ${mapAverage.toFixed(3)}`);
}

main();

export {};
