// This example shows reordering data and locating values with deliberate search logic.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

function binarySearch(values: number[], target: number): number {
    let left = 0;
    let right = values.length - 1;

    while (left <= right) {
        const middle = Math.floor((left + right) / 2);
        const value = values[middle]!;

        if (value === target) {
            return middle;
        }
        if (value < target) {
            left = middle + 1;
        } else {
            right = middle - 1;
        }
    }

    return -1;
}

const scores = [91, 77, 88, 64, 77, 95];
const ascending = [...scores].sort((left, right) => left - right);

console.log(`Original: ${scores.join(", ")}`);
console.log(`Sorted: ${ascending.join(", ")}`);
console.log(`Index of 88: ${binarySearch(ascending, 88)}`);
console.log(`Index of 70: ${binarySearch(ascending, 70)}`);

export {};
