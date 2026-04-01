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
    let bestWord = "";
    let bestCount = 0;

    for (const word of words) {
        const nextCount = (frequencies.get(word) ?? 0) + 1;
        frequencies.set(word, nextCount);
        if (nextCount > bestCount) {
            bestWord = word;
            bestCount = nextCount;
        }
    }

    console.log(`Most frequent: ${bestWord}`);
    console.log(`Count: ${bestCount}`);
}

main();
