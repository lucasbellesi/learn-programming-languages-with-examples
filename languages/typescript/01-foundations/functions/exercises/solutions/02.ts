import * as fs from "node:fs";
function countVowels(text: string): number {
    const vowels = new Set(["a", "e", "i", "o", "u"]);
    let total = 0;
    for (const character of text.toLowerCase()) {
        if (vowels.has(character)) {
            total += 1;
        }
    }
    return total;
}
console.log(countVowels(fs.readFileSync(0, "utf8").trimEnd()));
