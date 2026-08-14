using System;
using System.Collections.Generic;

abstract class Shape
{
    public abstract double Area();
    public abstract string Name();
}

sealed class Circle : Shape
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

    public override string Name()
    {
        return "Circle";
    }
}

sealed class Rectangle : Shape
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

    public override string Name()
    {
        return "Rectangle";
    }
}

class Program
{
    static void PrintList<T>(List<T> values, string label)
    {
        Console.Write(label + ": [");
        for (int index = 0; index < values.Count; index++)
        {
            Console.Write(values[index]);
            if (index + 1 < values.Count)
            {
                Console.Write(", ");
            }
        }

        Console.WriteLine("]");
    }

    static void Main()
    {
        List<Shape> shapes = new List<Shape>
        {
            new Circle(2.0),
            new Rectangle(3.0, 4.0),
            new Circle(1.5),
        };

        List<double> areas = new List<double>(shapes.Count);

        Console.WriteLine("Shape areas:");
        foreach (Shape shape in shapes)
        {
            double value = shape.Area();
            areas.Add(value);
            Console.WriteLine($"- {shape.Name()}: {value}");
        }

        double totalArea = 0.0;
        double minArea = areas[0];
        double maxArea = areas[0];

        foreach (double area in areas)
        {
            totalArea += area;
            if (area < minArea)
            {
                minArea = area;
            }

            if (area > maxArea)
            {
                maxArea = area;
            }
        }

        Console.WriteLine($"Total area: {totalArea}");
        Console.WriteLine($"Minimum area: {minArea}");
        Console.WriteLine($"Maximum area: {maxArea}");

        PrintList(new List<int> { 1, 2, 3, 4 }, "Sample counts");
        PrintList(areas, "Computed areas");
    }
}
