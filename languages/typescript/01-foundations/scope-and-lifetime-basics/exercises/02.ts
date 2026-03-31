import * as fs from "node:fs";
const [outerWord, innerWord] = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (!outerWord || !innerWord) {
    console.log("Expected: outerWord innerWord");
}
const label = outerWord;
console.log(`Outer before block: ${label}`);
{
    const label = innerWord;
    console.log(`Inner block: ${label}`);
}
console.log(`Outer after block: ${label}`);
