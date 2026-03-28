using System.Collections.Generic;

namespace ModularizationAndBuildStructureExample.Pricing;

public sealed class InvoiceSummary
{
    public InvoiceSummary(
        IReadOnlyList<LineItem> items,
        decimal subtotal,
        decimal discountValue,
        decimal fee,
        decimal finalTotal
    )
    {
        Items = items;
        Subtotal = subtotal;
        DiscountValue = discountValue;
        Fee = fee;
        FinalTotal = finalTotal;
    }

    public IReadOnlyList<LineItem> Items { get; }
    public decimal Subtotal { get; }
    public decimal DiscountValue { get; }
    public decimal Fee { get; }
    public decimal FinalTotal { get; }
}
