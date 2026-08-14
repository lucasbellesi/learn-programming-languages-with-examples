import * as fs from "node:fs";
const token = fs.readFileSync(0, "utf8").trim().toLowerCase();
const atIndex = token.indexOf("@");
if (atIndex <= 0 || atIndex === token.length - 1) {
    console.log("Expected a token shaped like name@domain.");
}
console.log(`${token.slice(0, atIndex)}@***`);
