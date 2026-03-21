using System;

class Program
{
    static void Main()
    {
        Console.Write("Subtotal: ");
        double subtotal = double.Parse(Console.ReadLine() ?? "0");

        Console.Write("Discount percent: ");
        double discountPercent = double.Parse(Console.ReadLine() ?? "0");

        Console.Write("Tax percent: ");
        double taxPercent = double.Parse(Console.ReadLine() ?? "0");

        if (subtotal < 0)
        {
            Console.WriteLine("Subtotal must be non-negative.");
            return;
        }

        double discountValue = subtotal * (discountPercent / 100.0);
        double discountedTotal = subtotal - discountValue;
        double taxValue = discountedTotal * (taxPercent / 100.0);
        double finalTotal = discountedTotal + taxValue;

        Console.WriteLine($"Discount value: {discountValue:F2}");
        Console.WriteLine($"Tax value: {taxValue:F2}");
        Console.WriteLine($"Final total: {finalTotal:F2}");
    }
}
