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
    const target = Number.parseInt(tokens[count + 1] ?? "", 10);

    if (
        values.length !== count ||
        values.some((value) => !Number.isInteger(value)) ||
        !Number.isInteger(target)
    ) {
        console.log("Invalid algorithm input.");
        return;
    }

    let foundIndex = -1;
    for (let index = 0; index < values.length; index += 1) {
        if (values[index] === target) {
            foundIndex = index;
            break;
        }
    }

    console.log(`First index: ${foundIndex}`);
}

main();
