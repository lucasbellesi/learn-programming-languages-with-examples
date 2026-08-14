import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    static class Rectangle {
        private final double width;
        private final double height;

        Rectangle(double width, double height) {
            if (width <= 0.0 || height <= 0.0) {
                throw new IllegalArgumentException("Dimensions must be positive.");
            }
            this.width = width;
            this.height = height;
        }

        double area() {
            return width * height;
        }

        double perimeter() {
            return 2.0 * (width + height);
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        double width = scanner.nextDouble();
        double height = scanner.nextDouble();

        try {
            Rectangle rectangle = new Rectangle(width, height);
            System.out.printf("Area: %.2f%n", rectangle.area());
            System.out.printf("Perimeter: %.2f%n", rectangle.perimeter());
        } catch (IllegalArgumentException error) {
            System.out.println(error.getMessage());
        }
    }
}
