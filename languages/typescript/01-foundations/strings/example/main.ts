// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: the example makes it possible to normalize, inspect, and transform textual data
// before the learner tackles the exercises.

const raw = "  TypeScript makes string cleanup explicit.  ";
const cleaned = raw.trim().toLowerCase();
const words = cleaned.split(/\s+/);
// The printed result shows whether the program can handle empty input and character boundaries
// safely.
console.log(`Cleaned: ${cleaned}`);
console.log(`Word count: ${words.length}`);
console.log(`Joined with dashes: ${words.join("-")}`);
export {};
