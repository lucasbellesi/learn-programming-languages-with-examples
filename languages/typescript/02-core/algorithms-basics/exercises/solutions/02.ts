import * as fs from "node:fs";

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
    if (
        values.length !== count ||
        values.some((value) => !Number.isInteger(value))
    ) {
        console.log("Invalid value list.");
        return;
    }

    let minimum = values[0]!;
    let maximum = values[0]!;
    let evenCount = 0;

    for (const value of values) {
        if (value < minimum) {
            minimum = value;
        }
        if (value > maximum) {
            maximum = value;
        }
        if (value % 2 === 0) {
            evenCount += 1;
        }
    }

    console.log(`Minimum: ${minimum}`);
    console.log(`Maximum: ${maximum}`);
    console.log(`Even count: ${evenCount}`);
}

main();
