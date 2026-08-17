import { readFileSync } from "node:fs";

function runPerformanceProfilingBasicsExercise(): void {
    const requestedSize = Number(readFileSync(0, "utf8").trim());
    // TODO 1: Validate requestedSize as a non-negative workload size.
    // TODO 2: Compare string concatenation with buffered joins.
    // TODO 3: Produce average milliseconds for both string-building approaches; verify workloads
    //         too small to show a meaningful difference.
    void requestedSize;
}

runPerformanceProfilingBasicsExercise();

export {};
