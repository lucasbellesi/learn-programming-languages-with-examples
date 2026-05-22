// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints easier to reason about.

type InventoryRecord = {
    name: string;
    counts: {
        inStock: number;
        reserved: number;
    };
};

function cloneInventory(record: InventoryRecord): InventoryRecord {
    // Clone nested data so later updates cannot leak back to the source object.
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

// These three names model aliasing, shallow copying, and deep copying side by side.
const alias = original;
const shallowCopy = { ...original };
const deepCopy = cloneInventory(original);

// Mutating each reference reveals which objects still share nested state.
alias.counts.inStock -= 1;
shallowCopy.counts.reserved += 3;
deepCopy.counts.inStock += 5;

// Report output values so learners can verify the copy and move semantics result.
console.log(`Original: ${original.counts.inStock}/${original.counts.reserved}`);
console.log(
    `Shallow copy: ${shallowCopy.counts.inStock}/${shallowCopy.counts.reserved}`,
);
console.log(
    `Deep copy: ${deepCopy.counts.inStock}/${deepCopy.counts.reserved}`,
);

export {};
