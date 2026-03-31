import * as fs from "node:fs";
const text = fs.readFileSync(0, "utf8").trim();
if (text.length === 0) {
    console.log(0);
}
console.log(text.split(/\s+/).filter((word) => word.length > 0).length);
