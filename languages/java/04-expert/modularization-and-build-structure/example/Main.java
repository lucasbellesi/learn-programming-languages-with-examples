// Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
// Why it matters: practicing modularization and build structure patterns makes exercises and checkpoints easier to reason about.

import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Main owns orchestration while sibling source files own calculation and formatting.
        List<LineItem> items = List.of(
                new LineItem("Notebook", 2, 3.50),
                new LineItem("Pencil", 5, 0.80),
                new LineItem("Backpack", 1, 29.99));

        InvoiceSummary summary = PricingService.summarize(items, 10.0, 7.5);

        // Report output through a formatter that receives data instead of reading global state.
        System.out.println(ReportFormatter.render(items, summary));
    }
}
