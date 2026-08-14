import * as fs from "node:fs";

abstract class Product {
    constructor(readonly price: number) {}
    abstract describe(): string;
}

class DigitalProduct extends Product {
    describe(): string {
        return `Digital: ${this.price.toFixed(2)}`;
    }
}

class PhysicalProduct extends Product {
    describe(): string {
        return `Physical: ${this.price.toFixed(2)}`;
    }
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const kind = tokens[0] ?? "";
    const price = Number.parseFloat(tokens[1] ?? "");
    if (Number.isNaN(price)) {
        console.log("Expected: kind price");
        return;
    }

    let product: Product | null = null;
    if (kind === "digital") {
        product = new DigitalProduct(price);
    } else if (kind === "physical") {
        product = new PhysicalProduct(price);
    }

    if (product === null) {
        console.log("Unknown product type.");
        return;
    }

    console.log(product.describe());
}

main();
