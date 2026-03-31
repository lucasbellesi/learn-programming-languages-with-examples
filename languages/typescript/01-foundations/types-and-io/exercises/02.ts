import * as fs from "node:fs";
const raw = fs.readFileSync(0, "utf8").trim();
const parts = raw.split(/\s+/);
if (parts.length < 3) {
    console.log("Expected: product price quantity");
}
const quantity = Number.parseInt(parts.pop() ?? "", 10);
const price = Number.parseFloat(parts.pop() ?? "");
const product = parts.join(" ");
if (
    !product ||
    Number.isNaN(price) ||
    !Number.isInteger(quantity) ||
    quantity < 0
) {
    console.log("Invalid invoice data.");
}
console.log(`Product: ${product}`);
console.log(`Quantity: ${quantity}`);
console.log(`Price: ${price.toFixed(2)}`);
console.log(`Total: ${(price * quantity).toFixed(2)}`);
