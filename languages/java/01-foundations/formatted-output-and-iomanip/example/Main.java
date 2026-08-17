// Module focus: Formatting values so output is easier to read and compare.
// Why it matters: the example makes it possible to produce stable human-readable tabular and
// numeric output before the learner tackles the exercises.

import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        String product = "Notebook";
        int quantity = 3;
        double price = 12.5;
        double total = quantity * price;

        // printf keeps columns and decimal places stable for learner-visible output.
        System.out.printf("%-12s %5s %8s %8s%n", "Product", "Qty", "Price", "Total");
        System.out.printf("%-12s %5d %8.2f %8.2f%n", product, quantity, price, total);
    }
}
