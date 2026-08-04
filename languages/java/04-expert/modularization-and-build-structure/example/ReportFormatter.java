// Presentation rules stay separate from pricing so either concern can change independently.

import java.util.List;
import java.util.Locale;

final class ReportFormatter {
    private ReportFormatter() {
    }

    static String render(List<LineItem> items, InvoiceSummary summary) {
        StringBuilder report = new StringBuilder("Invoice Summary\nItems:\n");
        for (LineItem item : items) {
            report.append(String.format(
                    Locale.ROOT,
                    "- %s: %d x %.2f%n",
                    item.name(),
                    item.quantity(),
                    item.unitPrice()));
        }

        report.append(String.format(Locale.ROOT, "Subtotal: %.2f%n", summary.subtotal()));
        report.append(String.format(Locale.ROOT, "Discount: %.2f%n", summary.discountValue()));
        report.append(String.format(Locale.ROOT, "Tax: %.2f%n", summary.taxValue()));
        report.append(String.format(Locale.ROOT, "Total: %.2f", summary.total()));
        return report.toString();
    }
}
