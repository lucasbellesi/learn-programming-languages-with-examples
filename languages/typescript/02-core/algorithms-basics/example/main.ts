// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: the example makes it possible to implement linear scans and accumulations with
// clear invariants before the learner tackles the exercises.

function firstIndexOf(values: number[], target: number): number {
    // A linear scan is the simplest search when the data is not sorted.
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
    // Seed summary values from real data so the loop handles negative values too.
    let minimum = values[0]!;
    let maximum = values[0]!;
    let evenCount = 0;

    // Keep one pass over the data and update each summary as evidence appears.
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
// The printed result shows whether the program can analyze behavior for empty, duplicate, and
// missing values.
console.log(`Values: ${values.join(", ")}`);
console.log(`First index of 14: ${firstIndexOf(values, 14)}`);
console.log(`Minimum: ${summary.minimum}`);
console.log(`Maximum: ${summary.maximum}`);
console.log(`Even count: ${summary.evenCount}`);

export {};
