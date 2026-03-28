using System;

sealed class InvoiceMath
{
    public decimal ComputeDiscount(decimal subtotal, decimal discountPercent)
    {
        return subtotal * discountPercent / 100.0m;
    }

    public decimal ComputeFinalTotal(decimal subtotal, decimal discountValue, decimal taxPercent)
    {
        decimal taxableBase = subtotal - discountValue;
        decimal taxValue = taxableBase * taxPercent / 100.0m;
        return taxableBase + taxValue;
    }
}

static class InvoicePrinter
{
    public static void Print(decimal subtotal, decimal discountValue, decimal finalTotal)
    {
        Console.WriteLine($"Subtotal: {subtotal:F2}");
        Console.WriteLine($"Discount: -{discountValue:F2}");
        Console.WriteLine($"Final total: {finalTotal:F2}");
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter subtotal, discount percent, and tax percent: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (
            parts.Length != 3
            || !decimal.TryParse(parts[0], out decimal subtotal)
            || !decimal.TryParse(parts[1], out decimal discountPercent)
            || !decimal.TryParse(parts[2], out decimal taxPercent)
        )
        {
            Console.WriteLine("Invalid input.");
            return;
        }

        if (
            subtotal < 0.0m
            || discountPercent < 0.0m
            || discountPercent > 100.0m
            || taxPercent < 0.0m
        )
        {
            Console.WriteLine("Values are out of range.");
            return;
        }

        InvoiceMath math = new InvoiceMath();
        decimal discountValue = math.ComputeDiscount(subtotal, discountPercent);
        decimal finalTotal = math.ComputeFinalTotal(subtotal, discountValue, taxPercent);

        InvoicePrinter.Print(subtotal, discountValue, finalTotal);
    }
}
