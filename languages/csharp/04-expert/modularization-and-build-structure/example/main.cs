// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: the example makes it possible to separate public contracts from implementation
// details before the learner tackles the exercises.

using System;
using ModularizationAndBuildStructureExample.Pricing;

// Separate helpers keep the main path focused on how to separate public contracts from
// implementation details.
class Program
{
    // Fixed inputs make the consequence of putting every class into `main.cs` even when
    // responsibilities diverge visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        LineItem[] items =
        {
            new LineItem("Notebook", 2, 3.50m),
            new LineItem("Pencil", 5, 0.80m),
            new LineItem("Backpack", 1, 29.99m),
        };

        InvoiceSummary summary = InvoiceCalculator.BuildSummary(items, 10.0m, 7.50m);

        // The printed result shows whether the program can organize a multi-file program with an
        // explicit build boundary.
        Console.WriteLine(InvoiceFormatter.Render(summary));
    }
}
