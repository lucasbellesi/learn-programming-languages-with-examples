import * as fs from "node:fs";
const tokens = fs.readFileSync(0, "utf8").trim().split(/\s+/);
const count = Number.parseInt(tokens[0] ?? "", 10);
if (!Number.isInteger(count) || count <= 0) {
    console.log("Count must be a positive integer.");
}
const values = tokens
    .slice(1, count + 1)
    .map((token) => Number.parseInt(token, 10));
if (
    values.length !== count ||
    values.some((value) => !Number.isInteger(value))
) {
    console.log("Missing or invalid integer values.");
}
console.log(values.reverse().join(" "));
