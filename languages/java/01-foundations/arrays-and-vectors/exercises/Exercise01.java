import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        int count = scanner.nextInt();
        int[] values = new int[count];
        int sum = 0;
        for (int i = 0; i < count; i++) {
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
