import * as fs from "node:fs";

class Pair<T> {
    constructor(
        readonly first: T,
        readonly second: T,
    ) {}

    describe(): string {
        return `${String(this.first)} | ${String(this.second)}`;
    }
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    if (tokens.length < 2) {
        console.log("Expected two values.");
        return;
    }

    const pair = new Pair(tokens[0]!, tokens[1]!);
    console.log(pair.describe());
}

main();
