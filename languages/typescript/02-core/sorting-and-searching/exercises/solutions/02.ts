import * as fs from "node:fs";

function binarySearch(values: number[], target: number): number {
    let left = 0;
    let right = values.length - 1;

    while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        const value = values[middle]!;

        if (value === target) {
            return middle;
        }
        if (value < target) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return -1;
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const count = Number.parseInt(tokens[0] ?? "", 10);
    if (!Number.isInteger(count) || count <= 0) {
        console.log("Count must be a positive integer.");
        return;
    }

    const values = tokens
        .slice(1, count + 1)
        .map((token) => Number.parseInt(token, 10));
    const target = Number.parseInt(tokens[count + 1] ?? "", 10);

    if (
        values.length !== count ||
        values.some((value) => !Number.isInteger(value)) ||
        !Number.isInteger(target)
    ) {
        console.log("Invalid search input.");
        return;
    }

    console.log(`Index: ${binarySearch(values, target)}`);
}

main();
