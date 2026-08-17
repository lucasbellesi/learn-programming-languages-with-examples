import { readFileSync } from "node:fs";

function runSmartPointersInDepthExercise(): void {
    const input = readFileSync(0, "utf8").trimEnd().split(/\r?\n/);
    // TODO 1: Parse the original theme, shortcuts, clone theme, and optional new shortcut.
    // TODO 2: Clone nested preferences before a local update.
    // TODO 3: Produce original and cloned preference states after editing only the clone; verify
    //         nested arrays or objects that would break a shallow copy.
    void input;
}

runSmartPointersInDepthExercise();

export {};
