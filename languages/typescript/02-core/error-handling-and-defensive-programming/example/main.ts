// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: practicing error handling and defensive programming patterns makes exercises and checkpoints easier to reason about.

type ScoreRecord = {
    name: string;
    score: number;
};

function parseRecord(line: string): ScoreRecord | null {
    // Treat the last field as the score so names can contain spaces.
    const parts = line.trim().split(/\s+/);
    if (parts.length < 2) {
        return null;
    }

    // Defensive parsing rejects non-numeric and out-of-range scores.
    const score = Number.parseInt(parts.at(-1) ?? "", 10);
    if (!Number.isInteger(score) || score < 0 || score > 100) {
        return null;
    }

    // A valid score is not enough; the record also needs a name.
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

// Process every row independently so one bad value does not stop the whole batch.
for (const row of rows) {
    const record = parseRecord(row);
    if (record === null) {
        // Report output values so learners can verify the error handling and defensive programming result.
        console.log(`Skipped invalid row: ${row}`);
        continue;
    }
    accepted.push(record);
}

// Report only records that survived every validation check.
console.log(`Accepted rows: ${accepted.length}`);
for (const record of accepted) {
    console.log(`- ${record.name}: ${record.score}`);
}

export {};
