// Pricing types and calculations live together so the domain boundary stays explicit.

import java.util.List;

final class PricingService {
    private PricingService() {
    }

    static InvoiceSummary summarize(
            List<LineItem> items,
            double discountPercent,
            double taxPercent) {
        if (discountPercent < 0.0 || discountPercent > 100.0 || taxPercent < 0.0) {
            throw new IllegalArgumentException("Pricing percentages are out of range.");
        }

        double subtotal = items.stream().mapToDouble(LineItem::total).sum();
        double discountValue = subtotal * discountPercent / 100.0;
        double taxableBase = subtotal - discountValue;
        double taxValue = taxableBase * taxPercent / 100.0;
        return new InvoiceSummary(
                subtotal,
                discountValue,
                taxValue,
                taxableBase + taxValue);
    }
}
