using System;
using System.Collections.Generic;

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
        List<Shape> shapes = new List<Shape>
        {
            new Rectangle(2.0, 5.0),
            new Circle(1.5)
        };

        double totalArea = 0.0;
        foreach (Shape shape in shapes)
        {
            totalArea += shape.Area();
        }

        Console.WriteLine($"Total area: {totalArea}");
    }
}
