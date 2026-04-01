import * as fs from "node:fs";

type InventoryRecord = {
    name: string;
    counts: {
        inStock: number;
        reserved: number;
    };
};

function cloneInventory(record: InventoryRecord): InventoryRecord {
    return {
        name: record.name,
        counts: {
            inStock: record.counts.inStock,
            reserved: record.counts.reserved,
        },
    };
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const name = tokens[0] ?? "";
    const inStock = Number.parseInt(tokens[1] ?? "", 10);
    const reserved = Number.parseInt(tokens[2] ?? "", 10);

    if (
        !name ||
        !Number.isInteger(inStock) ||
        !Number.isInteger(reserved) ||
        inStock < 0 ||
        reserved < 0
    ) {
        console.log("Expected: name inStock reserved");
        return;
    }

    const original: InventoryRecord = { name, counts: { inStock, reserved } };
    const cloned = cloneInventory(original);
    cloned.counts.inStock += 2;

    console.log(
        `Original: ${original.counts.inStock}/${original.counts.reserved}`,
    );
    console.log(`Cloned: ${cloned.counts.inStock}/${cloned.counts.reserved}`);
}

main();
