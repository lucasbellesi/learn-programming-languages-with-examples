import * as fs from "node:fs";
const raw = fs.readFileSync(0, "utf8").trim();
if (raw.length === 0) {
    console.log("Expected an integer count followed by values.");
}
const tokens = raw.split(/\s+/);
const count = Number.parseInt(tokens[0] ?? "", 10);
if (!Number.isInteger(count) || count <= 0) {
    console.log("Count must be a positive integer.");
}
const values = tokens
    .slice(1, count + 1)
    .map((token) => Number.parseFloat(token));
if (values.length !== count || values.some((value) => Number.isNaN(value))) {
    console.log("Missing or invalid numeric values.");
}
const sum = values.reduce((total, value) => total + value, 0);
console.log(`Sum: ${sum}`);
console.log(`Average: ${(sum / values.length).toFixed(2)}`);
console.log(`Minimum: ${Math.min(...values)}`);
console.log(`Maximum: ${Math.max(...values)}`);
