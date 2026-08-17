import { readFileSync } from "node:fs";

function runPerformanceProfilingBasicsExercise(): void {
    const requestedSize = Number(readFileSync(0, "utf8").trim());
    // TODO 1: Validate requestedSize as a non-negative record count.
    // TODO 2: Compare repeated array scans with `Map` lookups.
    // TODO 3: Produce average milliseconds for scan-based and map-based lookups; verify very small
    //         data sizes may hide the expected difference.
    void requestedSize;
}

runPerformanceProfilingBasicsExercise();

export {};
