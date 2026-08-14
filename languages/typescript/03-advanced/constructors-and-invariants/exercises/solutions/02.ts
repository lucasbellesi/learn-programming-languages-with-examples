import * as fs from "node:fs";

class TemperatureRange {
    constructor(
        readonly minimum: number,
        readonly maximum: number,
    ) {
        if (Number.isNaN(minimum) || Number.isNaN(maximum)) {
            throw new Error("Expected numeric temperatures.");
        }
        if (minimum > maximum) {
            throw new Error("Minimum cannot exceed maximum.");
        }
    }
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const minimum = Number.parseFloat(tokens[0] ?? "");
    const maximum = Number.parseFloat(tokens[1] ?? "");

    try {
        const range = new TemperatureRange(minimum, maximum);
        console.log(`Range: ${range.minimum}..${range.maximum}`);
    } catch (error) {
        console.log((error as Error).message);
    }
}

main();
