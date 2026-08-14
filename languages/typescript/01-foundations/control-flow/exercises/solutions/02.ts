import * as fs from "node:fs";
const start = Number.parseInt(fs.readFileSync(0, "utf8").trim(), 10);
if (!Number.isInteger(start) || start < 0) {
    console.log("Expected a non-negative integer.");
}
for (let current = start; current >= 0; current -= 1) {
    console.log(`Count: ${current}`);
}
console.log(start === 0 ? "Stopped immediately." : "Countdown complete.");
