// Use integer and decimal values to compute and print a score average.
// The example uses fixed data; the exercises introduce console input with Scanner.

import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Use fixed values so learners can focus on type conversions and output labels.
        int studentCount = 3;
        double firstScore = 91.0;
        double secondScore = 77.0;
        double thirdScore = 88.0;

        // A double total keeps the fractional part when dividing by an integer count.
        double total = firstScore + secondScore + thirdScore;
        double average = total / studentCount;

        // Print two decimal places so the total and average are easy to compare.
        System.out.println("Students: " + studentCount);
        System.out.printf("Total: %.2f%n", total);
        System.out.printf("Average: %.2f%n", average);
    }
}
