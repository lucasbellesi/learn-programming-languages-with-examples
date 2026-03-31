import * as fs from "node:fs";
const [leftText, rightText] = fs.readFileSync(0, "utf8").trim().split(/\s+/);
const left = Number.parseInt(leftText ?? "", 10);
const right = Number.parseInt(rightText ?? "", 10);
if (!Number.isInteger(left) || !Number.isInteger(right) || right === 0) {
    console.log("Expected two integers and a non-zero divisor.");
}
console.log(`Quotient: ${Math.trunc(left / right)}`);
console.log(`Remainder: ${left % right}`);
console.log(`Left is even: ${left % 2 === 0}`);
