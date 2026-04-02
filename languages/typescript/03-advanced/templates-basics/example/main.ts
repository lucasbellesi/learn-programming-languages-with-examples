// This example shows writing generic code that stays useful across multiple data types.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

function firstOrNull<T>(values: T[]): T | null {
    return values.length === 0 ? null : values[0]!;
}

class Box<T> {
    constructor(readonly value: T) {}

    describe(): string {
        return `Box(${String(this.value)})`;
    }
}

console.log(firstOrNull([1, 2, 3]));
console.log(firstOrNull(["go", "ts", "cpp"]));
console.log(new Box<number>(91).describe());
console.log(new Box<string>("Ana").describe());

export {};
