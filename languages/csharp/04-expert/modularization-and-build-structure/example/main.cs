// This example shows splitting responsibilities so entrypoints and helpers stay focused.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using ModularizationAndBuildStructureExample.Pricing;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes splitting responsibilities so entrypoints and helpers stay focused easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        LineItem[] items =
        {
            new LineItem("Notebook", 2, 3.50m),
            new LineItem("Pencil", 5, 0.80m),
            new LineItem("Backpack", 1, 29.99m),
        };

        InvoiceSummary summary = InvoiceCalculator.BuildSummary(items, 10.0m, 7.50m);

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine(InvoiceFormatter.Render(summary));
    }
}
