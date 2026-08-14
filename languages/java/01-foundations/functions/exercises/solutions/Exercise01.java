import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    static double area(double radius) {
        return Math.PI * radius * radius;
    }

    static double circumference(double radius) {
        return 2.0 * Math.PI * radius;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        double radius = scanner.nextDouble();
        System.out.printf("Area: %.2f%n", area(radius));
        System.out.printf("Circumference: %.2f%n", circumference(radius));
    }
}
