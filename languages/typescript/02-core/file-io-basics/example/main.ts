// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

import * as fs from "node:fs";
import * as path from "node:path";
import { buildScoreReport, parseScoreRow } from "./score-report";

// Explicit paths make missing input observable instead of creating it silently.
const sourcePath = path.resolve(
    process.argv[2] ?? path.join("example", "fixtures", "sample-scores.txt"),
);
const reportPath = path.resolve(
    process.argv[3] ?? path.join("build", "report.txt"),
);

if (!fs.existsSync(sourcePath)) {
    console.error(`Input file not found: ${sourcePath}`);
    process.exitCode = 1;
} else {
    const records = [];
    let invalidRows = 0;

    // Keep accepted and rejected records separate for transparent feedback.
    for (const line of fs.readFileSync(sourcePath, "utf8").split(/\r?\n/)) {
        if (line.trim().length === 0) {
            continue;
        }
        const record = parseScoreRow(line);
        if (record === null) {
            invalidRows++;
        } else {
            records.push(record);
        }
    }

    // Persist and print the same report so both outputs can be compared directly.
    const report = buildScoreReport(records, invalidRows);
    fs.mkdirSync(path.dirname(reportPath), { recursive: true });
    fs.writeFileSync(reportPath, report + "\n", "utf8");
    console.log(`Source file: ${sourcePath}`);
    console.log(`Report file: ${reportPath}`);
    console.log(report);
}
