import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Expected a value count.");
            return;
        }
        int count = scanner.nextInt();
        if (count <= 0) {
            System.out.println("Expected at least one value.");
            return;
        }
        int[] values = new int[count];
        long sum = 0;
        for (int i = 0; i < count; i++) {
            if (!scanner.hasNextInt()) {
                System.out.println("Missing value at position " + (i + 1) + ".");
                return;
            }
            values[i] = scanner.nextInt();
            sum += values[i];
        }
        int minimum = values[0];
        int maximum = values[0];
        for (int value : values) {
            minimum = Math.min(minimum, value);
            maximum = Math.max(maximum, value);
        }
        System.out.println("Sum: " + sum);
        System.out.printf("Average: %.2f%n", (double) sum / count);
        System.out.println("Minimum: " + minimum);
        System.out.println("Maximum: " + maximum);
    }
}
