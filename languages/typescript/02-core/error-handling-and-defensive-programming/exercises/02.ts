import * as fs from "node:fs";

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const accepted: number[] = [];
    for (const token of tokens) {
        const value = Number.parseInt(token, 10);
        if (!Number.isInteger(value)) {
            continue;
        }
        accepted.push(value);
    }

    if (accepted.length === 0) {
        console.log("No valid integers found.");
        return;
    }

    const total = accepted.reduce((sum, value) => sum + value, 0);
    console.log(`Valid count: ${accepted.length}`);
    console.log(`Average: ${(total / accepted.length).toFixed(2)}`);
}

main();
