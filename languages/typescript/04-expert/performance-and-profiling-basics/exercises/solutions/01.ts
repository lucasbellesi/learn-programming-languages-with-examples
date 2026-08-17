import { readFileSync } from "node:fs";
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
    const requestedSize = Number(readFileSync(0, "utf8").trim());
    const size =
        Number.isInteger(requestedSize) && requestedSize >= 0
            ? requestedSize
            : 0;
    const records: Pair[] = Array.from({ length: size }, (_, index) => ({
        key: `key-${index}`,
        value: index,
    }));
    const lookupMap = new Map(
        records.map((record) => [record.key, record.value]),
    );
    const runs = 12;

    const scanAverage = averageDuration(runs, () => {
        for (const target of [
            "key-0",
            `key-${Math.floor(size / 2)}`,
            `key-${size - 1}`,
        ]) {
            void records.find((record) => record.key === target)?.value;
        }
    });
    const mapAverage = averageDuration(runs, () => {
        for (const target of [
            "key-0",
            `key-${Math.floor(size / 2)}`,
            `key-${size - 1}`,
        ]) {
            void lookupMap.get(target);
        }
    });

    console.log(`Records: ${size}`);
    console.log(`Scan average (ms): ${scanAverage.toFixed(3)}`);
    console.log(`Map average (ms): ${mapAverage.toFixed(3)}`);
}

main();

export {};
