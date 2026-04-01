import { renderSummary } from "./formatting";
import { buildSummary, type LineItem } from "./pricing";

function main(): void {
    // Intent: keep orchestration here while calculations and formatting live elsewhere.
    const items: LineItem[] = [
        { name: "Notebook", quantity: 2, unitPrice: 3.5 },
        { name: "Pencil", quantity: 5, unitPrice: 0.8 },
        { name: "Backpack", quantity: 1, unitPrice: 29.99 },
    ];

    const summary = buildSummary(items, 10, 7.5);
    console.log(renderSummary(items, summary));
}

main();
