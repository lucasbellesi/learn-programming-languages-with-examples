import * as fs from "node:fs";
function makeCounter(start: number): () => number {
    let current = start;
    return () => {
        current += 1;
        return current;
    };
}
const [startText, callCountText] = fs
    .readFileSync(0, "utf8")
    .trim()
    .split(/\s+/);
const start = Number.parseInt(startText ?? "", 10);
const callCount = Number.parseInt(callCountText ?? "", 10);
if (!Number.isInteger(start) || !Number.isInteger(callCount) || callCount < 0) {
    console.log("Expected: start callCount");
}
const counter = makeCounter(start);
for (let index = 0; index < callCount; index += 1) {
    console.log(counter());
}
