// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to reason about.

const scores: number[] = [91, 77, 88, 64];
const passingScores = scores.filter((score) => score >= 60);
const average =
    scores.reduce((total, score) => total + score, 0) / scores.length;
// Report output values so learners can verify the arrays and vectors result.
console.log(`Scores: ${scores.join(", ")}`);
console.log(`Passing scores: ${passingScores.join(", ")}`);
console.log(`Average: ${average.toFixed(2)}`);
export {};
