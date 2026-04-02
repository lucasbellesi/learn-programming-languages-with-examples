// This helper example focuses on keeping presentation rules separate from calculations and program startup.

import type { InvoiceSummary, LineItem } from "./pricing";

export function renderSummary(
    items: LineItem[],
    summary: InvoiceSummary,
): string {
    const lines = ["Invoice Summary", "Items:"];

    for (const item of items) {
        lines.push(
            `- ${item.name}: ${item.quantity} x ${item.unitPrice.toFixed(2)}`,
        );
    }

    lines.push(`Subtotal: ${summary.subtotal.toFixed(2)}`);
    lines.push(`Discount: ${summary.discountValue.toFixed(2)}`);
    lines.push(`Tax: ${summary.taxValue.toFixed(2)}`);
    lines.push(`Total: ${summary.total.toFixed(2)}`);

    return lines.join("\n");
}
