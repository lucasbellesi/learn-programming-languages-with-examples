import { readFileSync } from "node:fs";

function runConcurrencyBasicsExercise(): void {
    const taskLines = readFileSync(0, "utf8").split(/\r?\n/);
    // TODO 1: Parse each non-empty line as `label delay-ms`.
    // TODO 2: Fetch several async results and preserve display order.
    // TODO 3: Produce completed task results in the original request order; verify mixed delays;
    //         one task finishing earlier than the first request.
    void taskLines;
}

runConcurrencyBasicsExercise();

export {};
