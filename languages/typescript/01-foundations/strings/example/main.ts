// This example shows cleaning and combining text while preserving readable string logic.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

const raw = "  TypeScript makes string cleanup explicit.  ";
const cleaned = raw.trim().toLowerCase();
const words = cleaned.split(/\s+/);
console.log(`Cleaned: ${cleaned}`);
console.log(`Word count: ${words.length}`);
console.log(`Joined with dashes: ${words.join("-")}`);
export {};
