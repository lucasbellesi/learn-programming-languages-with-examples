type ScoreRecord = {
    name: string;
    score: number;
};

function parseRecord(line: string): ScoreRecord | null {
    const parts = line.trim().split(/\s+/);
    if (parts.length < 2) {
        return null;
    }

    const score = Number.parseInt(parts.at(-1) ?? "", 10);
    if (!Number.isInteger(score) || score < 0 || score > 100) {
        return null;
    }

    const name = parts.slice(0, -1).join(" ");
    if (!name) {
        return null;
    }

    return { name, score };
}

const rows = [
    "Ana Smith 91",
    "InvalidRow",
    "Bob Lee ninety",
    "Carla Mendez 88",
];
const accepted: ScoreRecord[] = [];

for (const row of rows) {
    const record = parseRecord(row);
    if (record === null) {
        console.log(`Skipped invalid row: ${row}`);
        continue;
    }
    accepted.push(record);
}

console.log(`Accepted rows: ${accepted.length}`);
for (const record of accepted) {
    console.log(`- ${record.name}: ${record.score}`);
}

export {};
