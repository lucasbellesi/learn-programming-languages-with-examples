import * as fs from "node:fs";

function firstOrNull<T>(values: T[]): T | null {
    return values.length === 0 ? null : values[0]!;
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const first = firstOrNull(tokens);
    if (first === null) {
        console.log("Expected at least one value.");
        return;
    }

    console.log(`First: ${first}`);
}

main();
