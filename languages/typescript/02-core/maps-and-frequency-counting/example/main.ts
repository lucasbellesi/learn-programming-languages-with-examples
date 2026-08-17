// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: the example makes it possible to use key-value collections to aggregate and
// retrieve data before the learner tackles the exercises.

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

// The printed result shows whether the program can define normalization and missing-key behavior
// explicitly.
console.log(`Text: ${text}`);
for (const [word, count] of sortedEntries) {
    console.log(`${word}: ${count}`);
}

export {};
