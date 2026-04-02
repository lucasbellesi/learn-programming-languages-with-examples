// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: practicing formatted output and iomanip patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for formatted output and iomanip; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so formatted output and iomanip behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key formatted output and iomanip path.
        (string Name, int Quantity, double UnitPrice)[] items =
        {
            ("Notebook", 2, 3.5),
            ("Pencil", 5, 0.8),
            ("Backpack", 1, 29.99),
        };

        // Report values so learners can verify the formatted output and iomanip outcome.
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
