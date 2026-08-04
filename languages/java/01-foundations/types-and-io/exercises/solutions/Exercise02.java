import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) {
            System.out.println("Expected: product price quantity");
            return;
        }
        String product = scanner.next();
        double price = scanner.nextDouble();
        int quantity = scanner.nextInt();
        double total = price * quantity;
        System.out.println("Product: " + product);
        System.out.println("Quantity: " + quantity);
        System.out.printf("Total: %.2f%n", total);
    }
}
