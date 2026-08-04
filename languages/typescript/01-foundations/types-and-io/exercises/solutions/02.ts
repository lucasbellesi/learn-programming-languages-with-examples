import * as fs from "node:fs";

function main(): void {
    const raw = fs.readFileSync(0, "utf8").trim();
    const parts = raw.split(/\s+/);
    if (parts.length !== 3) {
        console.log("Invalid format. Use: product price quantity");
        return;
    }

    const product = parts[0];
    const price = Number.parseFloat(parts[1]);
    const quantity = Number.parseInt(parts[2], 10);
    if (Number.isNaN(price) || !Number.isInteger(quantity) || quantity < 0) {
        console.log("Invalid invoice data.");
        return;
    }

    console.log(`Product: ${product}`);
    console.log(`Quantity: ${quantity}`);
    console.log(`Price: ${price.toFixed(2)}`);
    console.log(`Total: ${(price * quantity).toFixed(2)}`);
}

main();
