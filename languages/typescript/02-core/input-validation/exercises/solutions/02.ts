import * as fs from "node:fs";

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const count = Number.parseInt(tokens[0] ?? "", 10);
    if (!Number.isInteger(count) || count < 1 || count > 50) {
        console.log("Score count must be an integer in range 1..50.");
        return;
    }

    const scores: number[] = [];
    for (const token of tokens.slice(1, count + 1)) {
        const score = Number.parseInt(token, 10);
        if (!Number.isInteger(score) || score < 0 || score > 100) {
            console.log("Every score must be an integer in range 0..100.");
            return;
        }
        scores.push(score);
    }

    if (scores.length !== count) {
        console.log("Missing score values.");
        return;
    }

    const total = scores.reduce((sum, score) => sum + score, 0);
    console.log(`Average: ${(total / scores.length).toFixed(2)}`);
}

main();
