import { readFileSync } from "node:fs";

function runSmartPointersInDepthExercise(): void {
    const [source = "empty", destination = "empty"] = readFileSync(0, "utf8")
        .trimEnd()
        .split(/\r?\n/);
    // TODO 1: Parse each holder as `tracking-id|weight` or `empty`.
    // TODO 2: Transfer an owned task between holders.
    // TODO 3: Produce holder state before and after transfer; verify moving from an empty holder;
    //         destination already occupied.
    void source;
    void destination;
}

runSmartPointersInDepthExercise();

export {};
