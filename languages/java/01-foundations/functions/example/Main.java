// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: the example makes it possible to decompose a problem into focused functions
// with explicit contracts before the learner tackles the exercises.

import java.util.Locale;

public class Main {
    static double average(int total, int count) {
        return (double) total / count;
    }

    static String statusFor(double average) {
        return average >= 80.0 ? "on track" : "needs practice";
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Main reads like a small story because helper methods hide reusable details.
        int total = 256;
        int count = 3;
        double average = average(total, count);

        System.out.printf("Average: %.2f%n", average);
        System.out.println("Status: " + statusFor(average));
    }
}
