// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: the example makes it possible to express reusable type-safe behavior with
// language generics before the learner tackles the exercises.

function firstOrNull<T>(values: T[]): T | null {
    return values.length === 0 ? null : values[0]!;
}

class Box<T> {
    constructor(readonly value: T) {}

    describe(): string {
        return `Box(${String(this.value)})`;
    }
}

// The printed result shows whether the program can apply constraints when an operation requires
// specific capabilities.
console.log(firstOrNull([1, 2, 3]));
console.log(firstOrNull(["go", "ts", "cpp"]));
console.log(new Box<number>(91).describe());
console.log(new Box<string>("Ana").describe());

export {};
