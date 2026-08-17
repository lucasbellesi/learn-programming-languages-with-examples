// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: the example makes it possible to decompose a problem into focused functions
// with explicit contracts before the learner tackles the exercises.

function formatLabel(value: number): string;
function formatLabel(value: string): string;
function formatLabel(value: number | string): string {
    return typeof value === "number" ? `Score: ${value}` : `Name: ${value}`;
}
function average(values: number[]): number {
    return values.reduce((total, value) => total + value, 0) / values.length;
}
console.log(formatLabel("Ana"));
console.log(formatLabel(91));
console.log(`Average: ${average([88, 91, 77]).toFixed(2)}`);
export {};
