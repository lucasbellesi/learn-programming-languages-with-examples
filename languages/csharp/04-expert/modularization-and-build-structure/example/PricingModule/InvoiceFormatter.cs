using System.Text;

namespace ModularizationAndBuildStructureExample.Pricing;

public static class InvoiceFormatter
{
    public static string Render(InvoiceSummary summary)
    {
        StringBuilder builder = new StringBuilder();

        builder.AppendLine("Invoice summary");
        builder.AppendLine("------------------------------");
        foreach (LineItem item in summary.Items)
        {
            builder.AppendLine(
                $"{item.Name, -12} qty={item.Quantity, 2} unit={item.UnitPrice, 6:F2} total={item.Total, 7:F2}"
            );
        }

        builder.AppendLine("------------------------------");
        builder.AppendLine($"Subtotal: {summary.Subtotal:F2}");
        builder.AppendLine($"Discount: -{summary.DiscountValue:F2}");
        builder.AppendLine($"Fee: +{summary.Fee:F2}");
        builder.AppendLine($"Final total: {summary.FinalTotal:F2}");

        return builder.ToString();
    }
}
