import * as fs from "node:fs";
const parts = fs.readFileSync(0, "utf8").trim().split(/\s+/);
if (parts.length < 3) {
    console.log("Expected: item quantity unitPrice");
}
const quantity = Number.parseInt(parts.pop() ?? "", 10);
const unitPrice = Number.parseFloat(parts.pop() ?? "");
const item = parts.join(" ");
if (
    !item ||
    !Number.isInteger(quantity) ||
    quantity < 0 ||
    Number.isNaN(unitPrice)
) {
    console.log("Invalid invoice data.");
}
console.log(
    `${item.padEnd(12, " ")} | ${String(quantity).padStart(3, " ")} | ${(quantity * unitPrice).toFixed(2).padStart(8, " ")}`,
);
