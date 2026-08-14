import * as fs from "node:fs";
const tokens = fs
    .readFileSync(0, "utf8")
    .trim()
    .split(/\s+/)
    .filter((token) => token.length > 0);
if (tokens.length === 0 || tokens.length % 2 !== 0) {
    console.log("Expected pairs of name and score.");
}
for (let index = 0; index < tokens.length; index += 2) {
    const name = tokens[index]!;
    const score = Number.parseFloat(tokens[index + 1]!);
    if (Number.isNaN(score)) {
        console.log("Invalid score in leaderboard input.");
    }
    console.log(`${name.padEnd(10, " ")} ${score.toFixed(1).padStart(6, " ")}`);
}
