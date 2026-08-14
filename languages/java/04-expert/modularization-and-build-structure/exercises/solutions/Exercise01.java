// Module focus: Separating invoice calculations from presentation responsibilities.
// Why it matters: focused types are easier to test and reuse than one large entrypoint.

import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    static final class InvoiceMath {
        double discount(double subtotal, double discountPercent) {
            return subtotal * discountPercent / 100.0;
        }

        double tax(double taxableBase, double taxPercent) {
            return taxableBase * taxPercent / 100.0;
        }
    }

    static final class InvoicePrinter {
        void print(double subtotal, double discount, double tax, double total) {
            System.out.printf(Locale.ROOT, "Subtotal: %.2f%n", subtotal);
            System.out.printf(Locale.ROOT, "Discount: -%.2f%n", discount);
            System.out.printf(Locale.ROOT, "Tax: %.2f%n", tax);
            System.out.printf(Locale.ROOT, "Final total: %.2f%n", total);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useLocale(Locale.ROOT);
        if (!scanner.hasNextDouble()) {
            System.out.println("Invalid subtotal.");
            return;
        }
        double subtotal = scanner.nextDouble();

        if (!scanner.hasNextDouble()) {
            System.out.println("Invalid discount percent.");
            return;
        }
        double discountPercent = scanner.nextDouble();

        if (!scanner.hasNextDouble()) {
            System.out.println("Invalid tax percent.");
            return;
        }
        double taxPercent = scanner.nextDouble();

        if (subtotal < 0.0
                || discountPercent < 0.0
                || discountPercent > 100.0
                || taxPercent < 0.0) {
            System.out.println("Values are out of range.");
            return;
        }

        InvoiceMath math = new InvoiceMath();
        double discount = math.discount(subtotal, discountPercent);
        double taxableBase = subtotal - discount;
        double tax = math.tax(taxableBase, taxPercent);
        new InvoicePrinter().print(subtotal, discount, tax, taxableBase + tax);
    }
}
