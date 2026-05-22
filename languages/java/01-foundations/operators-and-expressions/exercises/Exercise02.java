import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        double subtotal = scanner.nextDouble();
        double discountRate = scanner.nextDouble();
        double taxRate = scanner.nextDouble();
        double discount = subtotal * discountRate;
        double taxable = subtotal - discount;
        double tax = taxable * taxRate;
        System.out.printf("Discount: %.2f%n", discount);
        System.out.printf("Tax: %.2f%n", tax);
        System.out.printf("Total: %.2f%n", taxable + tax);
    }
}
