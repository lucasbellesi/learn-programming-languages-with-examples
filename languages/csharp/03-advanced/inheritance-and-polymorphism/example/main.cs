// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Collections.Generic;

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
    static void Main()
    {
        // Program flow: create mixed shapes and evaluate them through one base type.
        List<Shape> shapes = new List<Shape> { new Rectangle(3.0, 4.0), new Circle(2.0) };

        // Intent: polymorphic iteration keeps caller logic independent from concrete classes.
        foreach (Shape shape in shapes)
        {
            Console.WriteLine($"{shape.Name} area: {shape.Area():F2}");
        }
    }
}
