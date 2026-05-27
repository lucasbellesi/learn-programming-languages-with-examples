import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        String product = scanner.next();
        double price = scanner.nextDouble();
        int quantity = scanner.nextInt();
        System.out.printf("%-10s %5s %8s %8s%n", "Product", "Qty", "Price", "Total");
        System.out.printf("%-10s %5d %8.2f %8.2f%n", product, quantity, price, price * quantity);
    }
}
