// Example purpose: show the module flow with a separate reusable library project.

using System;
using ModularizationAndBuildStructureExample.Pricing;

class Program
{
    static void Main()
    {
        // Program flow: define input data, delegate calculations, then format a report.
        LineItem[] items =
        {
            new LineItem("Notebook", 2, 3.50m),
            new LineItem("Pencil", 5, 0.80m),
            new LineItem("Backpack", 1, 29.99m),
        };

        InvoiceSummary summary = InvoiceCalculator.BuildSummary(items, 10.0m, 7.50m);

        // Intent: keep console output in the entrypoint while reusable logic stays in the library.
        Console.WriteLine(InvoiceFormatter.Render(summary));
    }
}
