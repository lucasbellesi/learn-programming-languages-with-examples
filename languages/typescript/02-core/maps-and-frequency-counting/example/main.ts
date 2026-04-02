// This example shows counting repeated values and summarizing them through keyed lookups.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

const text = "go fast go far learn fast";
const words = text.split(/\s+/);
const frequencies = new Map<string, number>();

for (const word of words) {
    frequencies.set(word, (frequencies.get(word) ?? 0) + 1);
}

const sortedEntries = [...frequencies.entries()].sort((left, right) => {
    if (right[1] !== left[1]) {
        return right[1] - left[1];
    }
    return left[0].localeCompare(right[0]);
});

console.log(`Text: ${text}`);
for (const [word, count] of sortedEntries) {
    console.log(`${word}: ${count}`);
}

export {};
