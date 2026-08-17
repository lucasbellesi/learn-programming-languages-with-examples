import { readFileSync } from "node:fs";

function runMemoryManagementRaiiExercise(): void {
    const commands = readFileSync(0, "utf8").split(/\r?\n/);
    // TODO 1: Distinguish `record <message>` commands from `close` commands.
    // TODO 2: Enforce closed-state guardrails in a reusable session object.
    // TODO 3: Produce session logs before closing, after closing, and a guarded error message;
    //         verify repeated close calls; operations attempted after close.
    void commands;
}

runMemoryManagementRaiiExercise();

export {};
