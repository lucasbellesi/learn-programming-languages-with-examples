// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: practicing modularization and build structure patterns makes exercises and checkpoints easier to reason about.

using System;
using ModularizationAndBuildStructureExample.Pricing;

// Helper setup for modularization and build structure; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so modularization and build structure behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key modularization and build structure path.
        LineItem[] items =
        {
            new LineItem("Notebook", 2, 3.50m),
            new LineItem("Pencil", 5, 0.80m),
            new LineItem("Backpack", 1, 29.99m),
        };

        InvoiceSummary summary = InvoiceCalculator.BuildSummary(items, 10.0m, 7.50m);

        // Report values so learners can verify the modularization and build structure outcome.
        Console.WriteLine(InvoiceFormatter.Render(summary));
    }
}
