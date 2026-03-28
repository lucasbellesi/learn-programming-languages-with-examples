// This extra example extends operators and expressions with an invoice breakdown.
// Example purpose: combine arithmetic operations in a realistic pricing flow.

using System;

class Program
{
    static void Main()
    {
        double subtotal = 84.50;
        double discountPercent = 12.0;
        double taxPercent = 21.0;
        double shipping = 7.50;

        double discountValue = subtotal * discountPercent / 100.0;
        double taxableBase = subtotal - discountValue;
        double taxValue = taxableBase * taxPercent / 100.0;
        double finalTotal = taxableBase + taxValue + shipping;

        Console.WriteLine($"Subtotal: {subtotal:F2}");
        Console.WriteLine($"Discount: -{discountValue:F2}");
        Console.WriteLine($"Taxable base: {taxableBase:F2}");
        Console.WriteLine($"Tax: +{taxValue:F2}");
        Console.WriteLine($"Shipping: +{shipping:F2}");
        Console.WriteLine($"Final total: {finalTotal:F2}");
    }
}
