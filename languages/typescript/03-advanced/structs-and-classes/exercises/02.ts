import * as fs from "node:fs";

class InvoiceLine {
    constructor(
        readonly label: string,
        readonly quantity: number,
        readonly unitPrice: number,
    ) {}

    total(): number {
        return this.quantity * this.unitPrice;
    }
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const label = tokens[0] ?? "";
    const quantity = Number.parseInt(tokens[1] ?? "", 10);
    const unitPrice = Number.parseFloat(tokens[2] ?? "");

    if (!label || !Number.isInteger(quantity) || Number.isNaN(unitPrice)) {
        console.log("Expected: label quantity unitPrice");
        return;
    }
    if (quantity < 0 || unitPrice < 0) {
        console.log("Quantity and price must be non-negative.");
        return;
    }

    const line = new InvoiceLine(label, quantity, unitPrice);
    console.log(`Item: ${line.label}`);
    console.log(`Total: ${line.total().toFixed(2)}`);
}

main();
