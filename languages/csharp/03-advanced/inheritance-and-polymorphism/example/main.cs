// This example shows treating different concrete types through one common interface.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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
    // Run one deterministic scenario so the console output makes treating different concrete types through one common interface easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        List<Shape> shapes = new List<Shape> { new Rectangle(3.0, 4.0), new Circle(2.0) };

        foreach (Shape shape in shapes)
        {
            // Print the observed state here so learners can connect the code path to a concrete result.
            Console.WriteLine($"{shape.Name} area: {shape.Area():F2}");
        }
    }
}
