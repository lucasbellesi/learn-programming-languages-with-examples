// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: practicing formatted output and iomanip patterns makes exercises and checkpoints easier to reason about.

function formatRow(label: string, value: number): string {
    return `${label.padEnd(12, " ")} | ${value.toFixed(2).padStart(8, " ")}`;
}
console.log("Metric       |    Value");
console.log(formatRow("Average", 84.5));
console.log(formatRow("Minimum", 60));
console.log(formatRow("Maximum", 97));
export {};
