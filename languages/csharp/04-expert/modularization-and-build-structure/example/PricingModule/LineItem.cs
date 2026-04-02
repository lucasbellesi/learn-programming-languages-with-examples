// This helper example focuses on keeping the shared data model explicit so pricing logic stays readable.

namespace ModularizationAndBuildStructureExample.Pricing;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
public sealed class LineItem
{
    public LineItem(string name, int quantity, decimal unitPrice)
    {
        Name = name;
        Quantity = quantity;
        UnitPrice = unitPrice;
    }

    public string Name { get; }
    public int Quantity { get; }
    public decimal UnitPrice { get; }
    public decimal Total => Quantity * UnitPrice;
}
