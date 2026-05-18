// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

import * as fs from "node:fs";
import * as path from "node:path";

type ScoreRecord = {
    name: string;
    score: number;
};

function parseScoreRow(line: string): ScoreRecord | null {
    // Split on whitespace so names can contain spaces and the score stays last.
    const parts = line.trim().split(/\s+/);
    if (parts.length < 2) {
        return null;
    }

    // Reject rows where the final field is not an integer score.
    const score = Number.parseInt(parts.at(-1) ?? "", 10);
    if (!Number.isInteger(score)) {
        return null;
    }

    // Rejoin the remaining fields as the learner-visible name.
    const name = parts.slice(0, -1).join(" ");
    return name ? { name, score } : null;
}

const sourcePath = path.join(process.cwd(), "scores.txt");
const reportPath = path.join(process.cwd(), "report.txt");

// Create a small deterministic input file when the learner has not provided one yet.
if (!fs.existsSync(sourcePath)) {
    fs.writeFileSync(
        sourcePath,
        "Ana Smith 91\nBob Lee 77\nInvalidRow\nCarla Mendez 88\n",
        "utf8",
    );
}

const records: ScoreRecord[] = [];
let invalidRows = 0;

// Read the file the same way a checkpoint program would read a learner-provided path.
for (const line of fs.readFileSync(sourcePath, "utf8").split(/\r?\n/)) {
    // Empty lines are harmless formatting noise, not invalid data.
    if (line.trim().length === 0) {
        continue;
    }

    // Keep bad rows out of the report while still counting what was skipped.
    const record = parseScoreRow(line);
    if (record === null) {
        invalidRows++;
        continue;
    }

    records.push(record);
}

// Summarize the valid rows before writing the learner-facing report.
const total = records.reduce((sum, record) => sum + record.score, 0);
const average = records.length === 0 ? 0 : total / records.length;
const report = [
    "Grade Report",
    `Valid records: ${records.length}`,
    `Invalid rows skipped: ${invalidRows}`,
    `Average: ${average.toFixed(2)}`,
    ...records.map((record) => `- ${record.name}: ${record.score}`),
].join("\n");

fs.writeFileSync(reportPath, report + "\n", "utf8");

// Report output values so learners can inspect the file that was written.
console.log(`Source file: ${sourcePath}`);
console.log(`Report file: ${reportPath}`);
console.log(report);
