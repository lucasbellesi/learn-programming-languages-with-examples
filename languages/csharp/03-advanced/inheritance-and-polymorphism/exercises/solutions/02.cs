using System;
using System.Collections.Generic;
using System.Globalization;

abstract class Shape
{
    public abstract double Area();
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
}

class Program
{
    static void Main()
    {
        string[] tokens = Console
            .In.ReadToEnd()
            .Split(new[] { ' ', '\t', '\r', '\n' }, StringSplitOptions.RemoveEmptyEntries);
        int cursor = 0;
        if (tokens.Length == 0 || !int.TryParse(tokens[cursor++], out int count) || count < 0)
        {
            Console.WriteLine("Expected a non-negative shape count.");
            return;
        }

        List<Shape> shapes = new List<Shape>();
        for (int index = 0; index < count; index++)
        {
            if (cursor >= tokens.Length)
            {
                Console.WriteLine("Missing shape data.");
                return;
            }

            string kind = tokens[cursor++];
            if (kind == "rectangle")
            {
                if (
                    cursor + 1 >= tokens.Length
                    || !double.TryParse(
                        tokens[cursor++],
                        NumberStyles.Float,
                        CultureInfo.InvariantCulture,
                        out double width
                    )
                    || !double.TryParse(
                        tokens[cursor++],
                        NumberStyles.Float,
                        CultureInfo.InvariantCulture,
                        out double height
                    )
                )
                {
                    Console.WriteLine("Invalid rectangle.");
                    return;
                }
                shapes.Add(new Rectangle(width, height));
            }
            else if (kind == "circle")
            {
                if (
                    cursor >= tokens.Length
                    || !double.TryParse(
                        tokens[cursor++],
                        NumberStyles.Float,
                        CultureInfo.InvariantCulture,
                        out double radius
                    )
                )
                {
                    Console.WriteLine("Invalid circle.");
                    return;
                }
                shapes.Add(new Circle(radius));
            }
            else
            {
                Console.WriteLine("Unknown shape type.");
                return;
            }
        }

        double totalArea = 0.0;
        foreach (Shape shape in shapes)
        {
            totalArea += shape.Area();
        }

        Console.WriteLine($"Total area: {totalArea}");
    }
}
