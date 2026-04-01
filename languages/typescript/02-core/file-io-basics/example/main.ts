import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";

const tempDir = fs.mkdtempSync(path.join(os.tmpdir(), "ts-file-io-"));
const sourcePath = path.join(tempDir, "scores.txt");
const reportPath = path.join(tempDir, "report.txt");

try {
    fs.writeFileSync(sourcePath, "Ana 91\nBob 77\nCarla 88\n", "utf8");

    const scores = fs
        .readFileSync(sourcePath, "utf8")
        .split(/\r?\n/)
        .filter((line) => line.trim().length > 0)
        .map((line) => Number.parseInt(line.split(/\s+/).at(-1) ?? "", 10))
        .filter((score) => Number.isInteger(score));

    const average =
        scores.reduce((sum, score) => sum + score, 0) / scores.length;
    const report = [
        `Records: ${scores.length}`,
        `Average: ${average.toFixed(2)}`,
    ].join("\n");

    fs.writeFileSync(reportPath, report + "\n", "utf8");

    console.log(`Source file: ${sourcePath}`);
    console.log(`Report file: ${reportPath}`);
    console.log(report);
} finally {
    fs.rmSync(tempDir, { recursive: true, force: true });
}
