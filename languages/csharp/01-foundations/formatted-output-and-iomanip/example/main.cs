// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: the example makes it possible to produce stable human-readable tabular and
// numeric output before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to produce stable human-readable tabular and
// numeric output.
class Program
{
    // Fixed inputs make the consequence of producing unreadable tables with inconsistent widths
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        (string Name, int Quantity, double UnitPrice)[] items =
        {
            ("Notebook", 2, 3.5),
            ("Pencil", 5, 0.8),
            ("Backpack", 1, 29.99),
        };

        // The printed result shows whether the program can choose precision, alignment, and
        // labels appropriate to the data.
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
