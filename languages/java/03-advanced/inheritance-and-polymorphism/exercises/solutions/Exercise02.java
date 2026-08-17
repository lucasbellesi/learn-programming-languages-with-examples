import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class Exercise02 {
    interface Shape {
        double area();
    }

    static class Rectangle implements Shape {
        private final double width;
        private final double height;

        Rectangle(double width, double height) {
            this.width = width;
            this.height = height;
        }

        @Override
        public double area() {
            return width * height;
        }
    }

    static class Circle implements Shape {
        private final double radius;

        Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double area() {
            return Math.PI * radius * radius;
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Expected a non-negative shape count.");
            return;
        }
        int count = scanner.nextInt();
        if (count < 0) {
            System.out.println("Expected a non-negative shape count.");
            return;
        }

        List<Shape> shapes = new ArrayList<>();
        for (int index = 0; index < count; index++) {
            if (!scanner.hasNext()) {
                System.out.println("Missing shape data.");
                return;
            }
            String kind = scanner.next();
            if (kind.equals("rectangle")) {
                if (!scanner.hasNextDouble()) {
                    System.out.println("Invalid rectangle.");
                    return;
                }
                double width = scanner.nextDouble();
                if (!scanner.hasNextDouble()) {
                    System.out.println("Invalid rectangle.");
                    return;
                }
                shapes.add(new Rectangle(width, scanner.nextDouble()));
            } else if (kind.equals("circle")) {
                if (!scanner.hasNextDouble()) {
                    System.out.println("Invalid circle.");
                    return;
                }
                shapes.add(new Circle(scanner.nextDouble()));
            } else {
                System.out.println("Unknown shape type.");
                return;
            }
        }

        double totalArea = 0.0;
        for (Shape shape : shapes) {
            totalArea += shape.area();
        }

        System.out.printf("Total area: %.2f%n", totalArea);
    }
}
