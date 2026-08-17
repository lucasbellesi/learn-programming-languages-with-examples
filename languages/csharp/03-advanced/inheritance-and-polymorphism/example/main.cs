// Module focus: Treating different concrete types through one common interface.
// Why it matters: the example makes it possible to program against a shared behavioral
// abstraction before the learner tackles the exercises.

using System;
using System.Collections.Generic;

// Separate helpers keep the main path focused on how to program against a shared behavioral
// abstraction.
abstract class Shape
{
    // The base type names the behavior that every concrete shape must provide.
    public abstract double Area();
    public abstract string Name { get; }
}

class Rectangle : Shape
{
    private readonly double width;
    private readonly double height;

    public Rectangle(double widthValue, double heightValue) =>
        (width, height) = (widthValue, heightValue);

    public override double Area() => width * height;

    public override string Name => "Rectangle";
}

class Circle : Shape
{
    private readonly double radius;

    public Circle(double radiusValue) => radius = radiusValue;

    public override double Area() => Math.PI * radius * radius;

    public override string Name => "Circle";
}

class Program
{
    // Fixed inputs make the consequence of forgetting to mark base APIs as abstract or virtual
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        List<Shape> shapes = new List<Shape> { new Rectangle(3.0, 4.0), new Circle(2.0) };

        // The loop depends on the Shape contract, not on concrete type checks.
        foreach (Shape shape in shapes)
        {
            // The printed result shows whether the program can use dynamic dispatch without
            // unsafe type assumptions.
            Console.WriteLine($"{shape.Name} area: {shape.Area():F2}");
        }
    }
}
