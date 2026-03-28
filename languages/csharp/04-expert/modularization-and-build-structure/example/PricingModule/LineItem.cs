namespace ModularizationAndBuildStructureExample.Pricing;

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
