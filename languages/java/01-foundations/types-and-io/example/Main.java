// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: practicing types and io patterns makes exercises and checkpoints easier to reason about.

import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Use fixed values so learners can focus on type conversions and output labels.
        int studentCount = 3;
        double firstScore = 91.0;
        double secondScore = 77.0;
        double thirdScore = 88.0;

        double total = firstScore + secondScore + thirdScore;
        double average = total / studentCount;

        System.out.println("Students: " + studentCount);
        System.out.printf("Total: %.2f%n", total);
        System.out.printf("Average: %.2f%n", average);
    }
}
