import * as fs from "node:fs";

type ScoreRecord = {
    name: string;
    score: number;
};

function parseRow(line: string): ScoreRecord | null {
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

function main(): void {
    const inputPath = fs.readFileSync(0, "utf8").trim();
    if (!inputPath) {
        console.log("Expected an input file path.");
        return;
    }
    if (!fs.existsSync(inputPath)) {
        console.log("Input file not found.");
        return;
    }

    const validRecords: ScoreRecord[] = [];
    let invalidRows = 0;

    for (const line of fs.readFileSync(inputPath, "utf8").split(/\r?\n/)) {
        if (line.trim().length === 0) {
            continue;
        }

        const record = parseRow(line);
        if (record === null) {
            invalidRows += 1;
            continue;
        }

        validRecords.push(record);
    }

    const reportLines = [
        "Grade Report",
        `Source file: ${inputPath}`,
        `Valid records: ${validRecords.length}`,
        `Invalid rows skipped: ${invalidRows}`,
    ];

    if (validRecords.length === 0) {
        reportLines.push(
            "Average: N/A",
            "Minimum: N/A",
            "Maximum: N/A",
            "Students: none",
        );
        console.log("Valid records: 0");
        console.log(`Invalid rows skipped: ${invalidRows}`);
        console.log("Average: N/A");
    } else {
        const total = validRecords.reduce(
            (sum, record) => sum + record.score,
            0,
        );
        const minimum = validRecords.reduce(
            (best, record) => Math.min(best, record.score),
            validRecords[0]!.score,
        );
        const maximum = validRecords.reduce(
            (best, record) => Math.max(best, record.score),
            validRecords[0]!.score,
        );
        reportLines.push(
            `Average: ${(total / validRecords.length).toFixed(2)}`,
            `Minimum: ${minimum}`,
            `Maximum: ${maximum}`,
            "Students:",
        );
        for (const record of validRecords) {
            reportLines.push(`- ${record.name}: ${record.score}`);
        }

        console.log(`Valid records: ${validRecords.length}`);
        console.log(`Invalid rows skipped: ${invalidRows}`);
        console.log(`Average: ${(total / validRecords.length).toFixed(2)}`);
    }

    fs.writeFileSync("report.txt", reportLines.join("\n") + "\n", "utf8");
    console.log("Report written to report.txt");
}

main();
