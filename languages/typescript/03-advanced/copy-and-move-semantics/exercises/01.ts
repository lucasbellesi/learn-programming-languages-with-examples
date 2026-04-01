import * as fs from "node:fs";

type ProductRecord = {
    name: string;
    details: {
        quantity: number;
    };
};

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const name = tokens[0] ?? "";
    const quantity = Number.parseInt(tokens[1] ?? "", 10);
    if (!name || !Number.isInteger(quantity) || quantity < 0) {
        console.log("Expected: name nonNegativeQuantity");
        return;
    }

    const original: ProductRecord = { name, details: { quantity } };
    const copied = { ...original };
    copied.details.quantity += 1;

    console.log(`Original quantity: ${original.details.quantity}`);
    console.log(`Copied quantity: ${copied.details.quantity}`);
}

main();
