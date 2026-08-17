import { readFileSync } from "node:fs";
import { setTimeout as delay } from "node:timers/promises";

async function fetchLabel(label: string, waitMs: number): Promise<string> {
    await delay(waitMs);
    return `${label} ready`;
}

async function main(): Promise<void> {
    const tasks = readFileSync(0, "utf8")
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter((line) => line.length > 0)
        .map((line) => {
            const [label = "task", wait = "0"] = line.split(/\s+/);
            return fetchLabel(label, Number(wait));
        });

    if (tasks.length === 0) {
        console.log("No tasks.");
        return;
    }
    const labels = await Promise.all(tasks);

    for (const label of labels) {
        console.log(label);
    }
}

main().catch((error: unknown) => {
    if (error instanceof Error) {
        console.error(error.message);
    }
    process.exitCode = 1;
});
