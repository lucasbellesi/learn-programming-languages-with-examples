// Module focus: Treating different concrete types through one common interface.
// Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints easier to reason about.

import java.util.List;
import java.util.Locale;

public class Main {
    interface Shape {
        // The interface names the behavior generic code can rely on.
        double area();

        String name();
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
            // Each concrete class owns its formula behind the shared interface.
            return width * height;
        }

        @Override
        public String name() {
            return "Rectangle";
        }
    }

    static class Circle implements Shape {
        private final double radius;

        Circle(double radius) {
            this.radius = radius;
        }

        @Override
        public double area() {
            // Callers do not need to know this formula when they use Shape references.
            return Math.PI * radius * radius;
        }

        @Override
        public String name() {
            return "Circle";
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);

        // Prepare sample inputs that exercise the key inheritance and polymorphism path.
        List<Shape> shapes = List.of(new Rectangle(3.0, 4.0), new Circle(2.0));

        for (Shape shape : shapes) {
            // Report values so learners can verify the inheritance and polymorphism outcome.
            System.out.printf("%s area: %.2f%n", shape.name(), shape.area());
        }
    }
}
