import { setTimeout as delay } from "node:timers/promises";

async function fetchLabel(label: string, waitMs: number): Promise<string> {
    await delay(waitMs);
    return `${label} ready`;
}

async function main(): Promise<void> {
    const labels = await Promise.all([
        fetchLabel("alpha", 20),
        fetchLabel("beta", 5),
        fetchLabel("gamma", 12),
    ]);

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
