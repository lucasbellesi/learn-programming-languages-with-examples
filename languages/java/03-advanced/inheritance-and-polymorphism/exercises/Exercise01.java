import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    interface Shape {
        double area();
    }

    static class Triangle implements Shape {
        private final double base;
        private final double height;

        Triangle(double base, double height) {
            this.base = base;
            this.height = height;
        }

        @Override
        public double area() {
            return 0.5 * base * height;
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextDouble()) {
            System.out.println("Invalid input.");
            return;
        }
        double base = scanner.nextDouble();

        if (!scanner.hasNextDouble()) {
            System.out.println("Invalid input.");
            return;
        }
        double height = scanner.nextDouble();

        if (base <= 0.0 || height <= 0.0) {
            System.out.println("Base and height must be positive.");
            return;
        }

        Shape triangle = new Triangle(base, height);
        System.out.printf("Triangle area: %.2f%n", triangle.area());
    }
}
