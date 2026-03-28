using System;
using System.Collections.Generic;

namespace ModularizationAndBuildStructureExample.Pricing;

public static class InvoiceCalculator
{
    public static InvoiceSummary BuildSummary(
        IReadOnlyList<LineItem> items,
        decimal discountPercent,
        decimal fee
    )
    {
        decimal subtotal = 0.0m;
        foreach (LineItem item in items)
        {
            subtotal += item.Total;
        }

        decimal normalizedDiscount = Math.Clamp(discountPercent, 0.0m, 100.0m);
        decimal discountValue = subtotal * normalizedDiscount / 100.0m;
        decimal finalTotal = subtotal - discountValue + fee;

        return new InvoiceSummary(items, subtotal, discountValue, fee, finalTotal);
    }
}
