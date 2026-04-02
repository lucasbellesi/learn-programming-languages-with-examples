// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason about.

const raw = "  TypeScript makes string cleanup explicit.  ";
const cleaned = raw.trim().toLowerCase();
const words = cleaned.split(/\s+/);
// Report output values so learners can verify the strings result.
console.log(`Cleaned: ${cleaned}`);
console.log(`Word count: ${words.length}`);
console.log(`Joined with dashes: ${words.join("-")}`);
export {};
