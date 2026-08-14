import * as fs from "node:fs";

type StudentRecord = {
    name: string;
    score: number;
};

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

    const records: StudentRecord[] = [];
    let cursor = 1;
    for (let index = 0; index < count; index += 1) {
        const name = tokens[cursor++] ?? "";
        const score = Number.parseInt(tokens[cursor++] ?? "", 10);
        if (!name || !Number.isInteger(score)) {
            console.log("Invalid student record.");
            return;
        }
        records.push({ name, score });
    }

    for (const record of records) {
        console.log(`${record.name}: ${record.score}`);
    }
}

main();
