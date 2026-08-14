import * as fs from "node:fs";

function main(): void {
    const lines = fs
        .readFileSync(0, "utf8")
        .split(/\r?\n/)
        .map((line) => line.trim())
        .filter((line) => line.length > 0);

    const sourcePath = lines[0] ?? "";
    const destinationPath = lines[1] ?? "";
    if (!sourcePath || !destinationPath) {
        console.log("Expected source and destination paths.");
        return;
    }
    if (!fs.existsSync(sourcePath)) {
        console.log("Source file not found.");
        return;
    }

    const content = fs.readFileSync(sourcePath, "utf8").toUpperCase();
    fs.writeFileSync(destinationPath, content, "utf8");
    console.log(`Wrote uppercase copy to ${destinationPath}`);
}

main();
