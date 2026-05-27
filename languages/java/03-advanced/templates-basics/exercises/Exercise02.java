// Module focus: Applying a numeric type bound to a reusable average helper.
// Why it matters: bounded generics communicate what operations generic code is allowed to use.

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    static <T extends Number> double average(List<T> values) {
        if (values.isEmpty()) {
            return 0.0;
        }

        double total = 0.0;
        for (T value : values) {
            // Number gives the generic helper a common conversion path to double.
            total += value.doubleValue();
        }
        return total / values.size();
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid count.");
            return;
        }

        int count = scanner.nextInt();
        if (count < 0) {
            System.out.println("Count must not be negative.");
            return;
        }

        List<Double> values = new ArrayList<>();
        for (int index = 0; index < count; index++) {
            if (!scanner.hasNextDouble()) {
                System.out.println("Invalid value.");
                return;
            }
            values.add(scanner.nextDouble());
        }

        System.out.printf("Average: %.2f%n", average(values));
    }
}
