import * as fs from "node:fs";
const [subtotalText, loyaltyText] = fs
    .readFileSync(0, "utf8")
    .trim()
    .split(/\s+/);
const subtotal = Number.parseFloat(subtotalText ?? "");
if (
    Number.isNaN(subtotal) ||
    (loyaltyText !== "true" && loyaltyText !== "false")
) {
    console.log("Expected: subtotal loyaltyFlag");
}
const isLoyal = loyaltyText === "true";
const discountRate = subtotal >= 100 ? 0.1 : 0.05;
const loyaltyBonus = isLoyal ? 5 : 0;
console.log(
    `Final price: ${Math.max(0, subtotal - subtotal * discountRate - loyaltyBonus).toFixed(2)}`,
);
