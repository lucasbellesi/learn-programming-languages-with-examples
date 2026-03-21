// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        (string Name, int Quantity, double UnitPrice)[] items =
        {
            ("Notebook", 2, 3.5),
            ("Pencil", 5, 0.8),
            ("Backpack", 1, 29.99)
        };

        // Intent: print intermediate or final output for quick behavior verification.
        Console.WriteLine($"{"Item",-12}{"Qty",6}{"Unit",10}{"Total",10}");
        Console.WriteLine(new string('-', 38));

        double grandTotal = 0;
        // Intent: iterate through data in a clear and deterministic order.
        foreach (var item in items)
        {
            double total = item.Quantity * item.UnitPrice;
            grandTotal += total;
            Console.WriteLine($"{item.Name,-12}{item.Quantity,6}{item.UnitPrice,10:F2}{total,10:F2}");
        }

        Console.WriteLine(new string('-', 38));
        Console.WriteLine($"{"Grand total",-28}{grandTotal,10:F2}");
    }
}
