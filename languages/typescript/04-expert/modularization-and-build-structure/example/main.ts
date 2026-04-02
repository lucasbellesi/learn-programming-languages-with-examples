// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: practicing modularization and build structure patterns makes exercises and checkpoints easier to reason about.

import { renderSummary } from "./formatting";
import { buildSummary, type LineItem } from "./pricing";

// Walk through one fixed scenario so modularization and build structure behavior stays repeatable.
function main(): void {
    // Prepare sample inputs that exercise the key modularization and build structure path.
    const items: LineItem[] = [
        { name: "Notebook", quantity: 2, unitPrice: 3.5 },
        { name: "Pencil", quantity: 5, unitPrice: 0.8 },
        { name: "Backpack", quantity: 1, unitPrice: 29.99 },
    ];

    const summary = buildSummary(items, 10, 7.5);
    // Report values so learners can verify the modularization and build structure outcome.
    console.log(renderSummary(items, summary));
}

main();
