// This example shows how copying, sharing, or transferring state changes later behavior.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

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

const original: InventoryRecord = {
    name: "Keyboard",
    counts: { inStock: 10, reserved: 2 },
};

const alias = original;
const shallowCopy = { ...original };
const deepCopy = cloneInventory(original);

alias.counts.inStock -= 1;
shallowCopy.counts.reserved += 3;
deepCopy.counts.inStock += 5;

console.log(`Original: ${original.counts.inStock}/${original.counts.reserved}`);
console.log(
    `Shallow copy: ${shallowCopy.counts.inStock}/${shallowCopy.counts.reserved}`,
);
console.log(
    `Deep copy: ${deepCopy.counts.inStock}/${deepCopy.counts.reserved}`,
);

export {};
