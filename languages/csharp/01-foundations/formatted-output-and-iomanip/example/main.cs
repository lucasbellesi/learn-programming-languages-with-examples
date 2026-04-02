// This example shows formatting values so output is easier to read and compare.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes formatting values so output is easier to read and compare easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        (string Name, int Quantity, double UnitPrice)[] items =
        {
            ("Notebook", 2, 3.5),
            ("Pencil", 5, 0.8),
            ("Backpack", 1, 29.99),
        };

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"{"Item", -12}{"Qty", 6}{"Unit", 10}{"Total", 10}");
        Console.WriteLine(new string('-', 38));

        double grandTotal = 0;
        foreach (var item in items)
        {
            double total = item.Quantity * item.UnitPrice;
            grandTotal += total;
            Console.WriteLine(
                $"{item.Name, -12}{item.Quantity, 6}{item.UnitPrice, 10:F2}{total, 10:F2}"
            );
        }

        Console.WriteLine(new string('-', 38));
        Console.WriteLine($"{"Grand total", -28}{grandTotal, 10:F2}");
    }
}
