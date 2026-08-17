import { readFileSync } from "node:fs";

function runConcurrencyBasicsExercise(): void {
    const [limitLine = "1", ...jobLines] = readFileSync(0, "utf8")
        .trimEnd()
        .split(/\r?\n/);
    // TODO 1: Validate the worker limit and parse the remaining lines as delays.
    // TODO 2: Process jobs with a maximum of two active workers.
    // TODO 3: Produce worker start/finish logs plus a final ordered summary; verify fewer jobs than
    //         workers; an empty job list.
    void limitLine;
    void jobLines;
}

runConcurrencyBasicsExercise();

export {};
