import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        if (count <= 0) {
            System.out.println("Count must be positive.");
            return;
        }
        double sum = 0.0;
        double minimum = Double.POSITIVE_INFINITY;
        double maximum = Double.NEGATIVE_INFINITY;
        for (int i = 0; i < count; i++) {
            double value = scanner.nextDouble();
            sum += value;
            minimum = Math.min(minimum, value);
            maximum = Math.max(maximum, value);
        }
        System.out.printf("Sum: %.2f%n", sum);
        System.out.printf("Average: %.2f%n", sum / count);
        System.out.printf("Minimum: %.2f%n", minimum);
        System.out.printf("Maximum: %.2f%n", maximum);
    }
}
