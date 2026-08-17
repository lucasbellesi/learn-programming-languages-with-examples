import { readFileSync } from "node:fs";

function runMemoryManagementRaiiExercise(): void {
    const [label = "buffer", chunkLine = "", mode = "success"] = readFileSync(
        0,
        "utf8",
    )
        .trimEnd()
        .split(/\r?\n/);
    // TODO 1: Parse chunkLine as comma-separated work and validate mode.
    // TODO 2: Use `try/finally` to close a temporary resource safely.
    // TODO 3: Produce setup, work, and cleanup messages in the correct order; verify cleanup must
    //         still happen after a simulated failure.
    void label;
    void chunkLine;
    void mode;
}

runMemoryManagementRaiiExercise();

export {};
