// Module focus: Combining values through expressions and readable calculations.
// Why it matters: practicing operators and expressions patterns makes exercises and checkpoints easier to reason about.

import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Parentheses make the order of operations visible before Java applies precedence.
        double subtotal = 120.0;
        double discountRate = 0.15;
        double taxRate = 0.08;

        double discount = subtotal * discountRate;
        double taxable = subtotal - discount;
        double tax = taxable * taxRate;
        double total = taxable + tax;

        // Report each calculated amount with fixed decimals for deterministic output.
        System.out.printf("Discount: %.2f%n", discount);
        System.out.printf("Tax: %.2f%n", tax);
        System.out.printf("Total: %.2f%n", total);
    }
}
