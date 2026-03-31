const raw = "  TypeScript makes string cleanup explicit.  ";
const cleaned = raw.trim().toLowerCase();
const words = cleaned.split(/\s+/);
console.log(`Cleaned: ${cleaned}`);
console.log(`Word count: ${words.length}`);
console.log(`Joined with dashes: ${words.join("-")}`);
export {};
