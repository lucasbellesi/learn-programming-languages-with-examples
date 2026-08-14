import * as fs from "node:fs";

function main(): void {
    const filePath = fs.readFileSync(0, "utf8").trim();
    if (!filePath) {
        console.log("Expected a file path.");
        return;
    }
    if (!fs.existsSync(filePath)) {
        console.log("Input file not found.");
        return;
    }

    const nonEmptyLines = fs
        .readFileSync(filePath, "utf8")
        .split(/\r?\n/)
        .filter((line) => line.trim().length > 0);

    console.log(`Non-empty lines: ${nonEmptyLines.length}`);
}

main();
