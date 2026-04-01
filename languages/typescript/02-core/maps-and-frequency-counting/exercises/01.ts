import * as fs from "node:fs";

function main(): void {
    const words = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((word) => word.length > 0);

    if (words.length === 0) {
        console.log("Expected at least one word.");
        return;
    }

    const frequencies = new Map<string, number>();
    for (const word of words) {
        frequencies.set(word, (frequencies.get(word) ?? 0) + 1);
    }

    for (const [word, count] of frequencies.entries()) {
        console.log(`${word}: ${count}`);
    }
}

main();
