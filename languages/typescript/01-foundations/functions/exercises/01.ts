import * as fs from "node:fs";
function maxOfThree(a: number, b: number, c: number): number {
    return Math.max(a, b, c);
}
const values = fs
    .readFileSync(0, "utf8")
    .trim()
    .split(/\s+/)
    .map((token) => Number.parseInt(token, 10));
if (values.length < 3 || values.some((value) => !Number.isInteger(value))) {
    console.log("Expected three integers.");
}
console.log(maxOfThree(values[0]!, values[1]!, values[2]!));
