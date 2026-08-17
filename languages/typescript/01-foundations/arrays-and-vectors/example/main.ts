// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: the example makes it possible to store and traverse ordered collections safely
// before the learner tackles the exercises.

const scores: number[] = [91, 77, 88, 64];
const passingScores = scores.filter((score) => score >= 60);
const average =
    scores.reduce((total, score) => total + score, 0) / scores.length;
// The printed result shows whether the program can handle empty collections and index boundaries
// explicitly.
console.log(`Scores: ${scores.join(", ")}`);
console.log(`Passing scores: ${passingScores.join(", ")}`);
console.log(`Average: ${average.toFixed(2)}`);
export {};
