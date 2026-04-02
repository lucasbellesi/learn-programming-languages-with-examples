// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to reason about.

function firstIndexOf(values: number[], target: number): number {
    for (let index = 0; index < values.length; index += 1) {
        if (values[index] === target) {
            return index;
        }
    }
    return -1;
}

function summarize(values: number[]): {
    minimum: number;
    maximum: number;
    evenCount: number;
} {
    let minimum = values[0]!;
    let maximum = values[0]!;
    let evenCount = 0;

    for (const value of values) {
        if (value < minimum) {
            minimum = value;
        }
        if (value > maximum) {
            maximum = value;
        }
        if (value % 2 === 0) {
            evenCount += 1;
        }
    }

    return { minimum, maximum, evenCount };
}

const values = [14, 7, 22, 14, 9, 18];
const summary = summarize(values);
// Report output values so learners can verify the algorithms basics result.
console.log(`Values: ${values.join(", ")}`);
console.log(`First index of 14: ${firstIndexOf(values, 14)}`);
console.log(`Minimum: ${summary.minimum}`);
console.log(`Maximum: ${summary.maximum}`);
console.log(`Even count: ${summary.evenCount}`);

export {};
