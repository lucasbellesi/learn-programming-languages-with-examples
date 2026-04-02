// This example shows splitting responsibilities so entrypoints and helpers stay focused.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

import { renderSummary } from "./formatting";
import { buildSummary, type LineItem } from "./pricing";

// Run one deterministic scenario so the console output makes splitting responsibilities so entrypoints and helpers stay focused easy to verify.
function main(): void {
    // Build the sample state first, then let the later output confirm the behavior step by step.
    const items: LineItem[] = [
        { name: "Notebook", quantity: 2, unitPrice: 3.5 },
        { name: "Pencil", quantity: 5, unitPrice: 0.8 },
        { name: "Backpack", quantity: 1, unitPrice: 29.99 },
    ];

    const summary = buildSummary(items, 10, 7.5);
    // Print the observed state here so learners can connect the code path to a concrete result.
    console.log(renderSummary(items, summary));
}

main();
