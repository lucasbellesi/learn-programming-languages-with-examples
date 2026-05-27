import java.util.List;
import java.util.Locale;

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
        List<Shape> shapes = List.of(new Rectangle(2.0, 5.0), new Circle(1.5));

        double totalArea = 0.0;
        for (Shape shape : shapes) {
            totalArea += shape.area();
        }

        System.out.printf("Total area: %.2f%n", totalArea);
    }
}
