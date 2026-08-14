import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        double left = scanner.nextDouble();
        double right = scanner.nextDouble();
        System.out.printf("Sum: %.2f%n", left + right);
        System.out.printf("Difference: %.2f%n", left - right);
        System.out.printf("Product: %.2f%n", left * right);
        if (right == 0.0) {
            System.out.println("Quotient: undefined");
        } else {
            System.out.printf("Quotient: %.2f%n", left / right);
        }
    }
}
