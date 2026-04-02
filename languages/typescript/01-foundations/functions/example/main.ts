// This example shows breaking behavior into reusable functions with clear inputs and outputs.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

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
