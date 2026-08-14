import * as fs from "node:fs";
const words = fs
    .readFileSync(0, "utf8")
    .trim()
    .split(/\s+/)
    .filter((word) => word.length > 0);
if (words.length === 0) {
    console.log("Expected at least one word.");
}
const seen = new Set<string>();
const unique: string[] = [];
for (const word of words) {
    if (!seen.has(word)) {
        seen.add(word);
        unique.push(word);
    }
}
console.log(unique.join(" "));
