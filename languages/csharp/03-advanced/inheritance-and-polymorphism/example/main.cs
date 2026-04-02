// Module focus: Treating different concrete types through one common interface.
// Why it matters: practicing inheritance and polymorphism patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for inheritance and polymorphism; this keeps the walkthrough readable.
abstract class Shape
{
    public abstract double Area();
    public abstract string Name { get; }
}

class Rectangle : Shape
{
    private readonly double width;
    private readonly double height;

    public Rectangle(double widthValue, double heightValue)
    {
        width = widthValue;
        height = heightValue;
    }

    public override double Area()
    {
        return width * height;
    }

    public override string Name => "Rectangle";
}

class Circle : Shape
{
    private readonly double radius;

    public Circle(double radiusValue)
    {
        radius = radiusValue;
    }

    public override double Area()
    {
        return Math.PI * radius * radius;
    }

    public override string Name => "Circle";
}

class Program
{
    // Walk through one fixed scenario so inheritance and polymorphism behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key inheritance and polymorphism path.
        List<Shape> shapes = new List<Shape> { new Rectangle(3.0, 4.0), new Circle(2.0) };

        foreach (Shape shape in shapes)
        {
            // Report values so learners can verify the inheritance and polymorphism outcome.
            Console.WriteLine($"{shape.Name} area: {shape.Area():F2}");
        }
    }
}
