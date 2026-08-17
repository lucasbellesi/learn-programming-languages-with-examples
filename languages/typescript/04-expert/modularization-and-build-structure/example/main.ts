// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: the example makes it possible to separate public contracts from implementation
// details before the learner tackles the exercises.

import { renderSummary } from "./formatting";
import { buildSummary, type LineItem } from "./pricing";

// Fixed inputs make the consequence of leaving all logic in `main.ts` and calling it modular
// visible and repeatable.
function main(): void {
    // These values exercise the normal path before the exercises vary the documented boundaries.
    const items: LineItem[] = [
        { name: "Notebook", quantity: 2, unitPrice: 3.5 },
        { name: "Pencil", quantity: 5, unitPrice: 0.8 },
        { name: "Backpack", quantity: 1, unitPrice: 29.99 },
    ];

    const summary = buildSummary(items, 10, 7.5);
    // The printed result shows whether the program can organize a multi-file program with an
    // explicit build boundary.
    console.log(renderSummary(items, summary));
}

main();
