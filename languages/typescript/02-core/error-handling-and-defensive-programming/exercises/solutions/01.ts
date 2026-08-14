import * as fs from "node:fs";

function main(): void {
    const line = fs.readFileSync(0, "utf8").trim();
    const parts = line.split(/\s+/);
    if (parts.length < 2) {
        console.log("Expected: Full Name Score");
        return;
    }

    const score = Number.parseInt(parts.at(-1) ?? "", 10);
    const name = parts.slice(0, -1).join(" ");
    if (!name || !Number.isInteger(score) || score < 0 || score > 100) {
        console.log("Invalid record.");
        return;
    }

    console.log(`Accepted: ${name} (${score})`);
}

main();
