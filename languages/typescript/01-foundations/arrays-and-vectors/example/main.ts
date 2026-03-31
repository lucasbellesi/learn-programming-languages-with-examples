const scores: number[] = [91, 77, 88, 64];
const passingScores = scores.filter((score) => score >= 60);
const average =
    scores.reduce((total, score) => total + score, 0) / scores.length;
console.log(`Scores: ${scores.join(", ")}`);
console.log(`Passing scores: ${passingScores.join(", ")}`);
console.log(`Average: ${average.toFixed(2)}`);
export {};
