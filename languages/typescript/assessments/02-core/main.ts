import * as fs from "node:fs";

function bucketForScore(score: number): number {
    return score === 100 ? 9 : Math.floor(score / 10);
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .split(/\s+/)
        .map((token) => token.trim())
        .filter((token) => token.length > 0);

    const values: number[] = [];
    const buckets = Array.from({ length: 10 }, () => 0);

    for (const token of tokens) {
        const value = Number.parseInt(token, 10);
        if (!Number.isInteger(value)) {
            console.log(`Ignoring invalid token: ${token}`);
            continue;
        }
        if (value === -1) {
            break;
        }
        if (value < 0 || value > 100) {
            console.log(`Ignoring out-of-range value: ${value}`);
            continue;
        }

        values.push(value);
        buckets[bucketForScore(value)] += 1;
    }

    const lines: string[] = [];
    if (values.length === 0) {
        lines.push("No valid values were entered.");
        lines.push("Report saved to core_assessment_report.txt");
    } else {
        const total = values.reduce((sum, value) => sum + value, 0);
        const minimum = values.reduce(
            (best, value) => Math.min(best, value),
            values[0]!,
        );
        const maximum = values.reduce(
            (best, value) => Math.max(best, value),
            values[0]!,
        );

        lines.push(`Valid count: ${values.length}`);
        lines.push(`Minimum: ${minimum}`);
        lines.push(`Maximum: ${maximum}`);
        lines.push(`Average: ${total / values.length}`);
        lines.push("Frequency table:");

        for (let index = 0; index < buckets.length; index += 1) {
            const start = index * 10;
            const end = index === 9 ? 100 : start + 9;
            lines.push(`${start}-${end}: ${buckets[index]}`);
        }

        lines.push("Report saved to core_assessment_report.txt");
    }

    for (const line of lines) {
        console.log(line);
    }
    fs.writeFileSync(
        "core_assessment_report.txt",
        lines.join("\n") + "\n",
        "utf8",
    );
}

main();
