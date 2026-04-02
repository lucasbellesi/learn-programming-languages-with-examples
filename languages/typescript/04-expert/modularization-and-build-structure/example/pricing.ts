// This helper example focuses on keeping pricing logic separate from orchestration and output code.

export type LineItem = {
    name: string;
    quantity: number;
    unitPrice: number;
};

export type InvoiceSummary = {
    subtotal: number;
    discountValue: number;
    taxValue: number;
    total: number;
};

export function buildSummary(
    items: LineItem[],
    discountPercent: number,
    taxPercent: number,
): InvoiceSummary {
    const subtotal = items.reduce(
        (sum, item) => sum + item.quantity * item.unitPrice,
        0,
    );
    const discountValue = subtotal * (discountPercent / 100);
    const taxedBase = subtotal - discountValue;
    const taxValue = taxedBase * (taxPercent / 100);

    return {
        subtotal,
        discountValue,
        taxValue,
        total: taxedBase + taxValue,
    };
}
