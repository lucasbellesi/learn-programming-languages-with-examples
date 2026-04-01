import * as fs from "node:fs";

function main(): void {
    const raw = fs.readFileSync(0, "utf8").trim();
    const value = Number.parseInt(raw, 10);

    if (!Number.isInteger(value)) {
        console.log("Expected one integer.");
        return;
    }
    if (value < 1 || value > 100) {
        console.log("Value must be in range 1..100.");
        return;
    }

    console.log(`Square: ${value * value}`);
}

main();
