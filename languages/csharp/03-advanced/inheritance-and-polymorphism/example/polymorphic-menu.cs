// This helper example focuses on isolating one polymorphic dispatch path so the common interface stays clear.

// This extra example extends inheritance-and-polymorphism with a polymorphic menu.

using System;
using System.Collections.Generic;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
abstract class Shape
{
    public abstract double Area();

    public abstract string Name();
}

class Circle : Shape
{
    public Circle(double radiusValue)
    {
        Radius = radiusValue;
    }

    private double Radius { get; }

    public override double Area()
    {
        return 3.1415926535 * Radius * Radius;
    }

    public override string Name()
    {
        return "Circle";
    }
}

class Rectangle : Shape
{
    public Rectangle(double widthValue, double heightValue)
    {
        Width = widthValue;
        Height = heightValue;
    }

    private double Width { get; }

    private double Height { get; }

    public override double Area()
    {
        return Width * Height;
    }

    public override string Name()
    {
        return "Rectangle";
    }
}

class Program
{
    static void Main()
    {
        List<Shape> shapes = new List<Shape>();

        while (true)
        {
            Console.WriteLine("\nMenu");
            Console.WriteLine("1) Add circle");
            Console.WriteLine("2) Add rectangle");
            Console.WriteLine("3) List areas");
            Console.WriteLine("4) Exit");
            Console.Write("Choose: ");

            string? option = Console.ReadLine();
            if (option == "1")
            {
                Console.Write("Radius: ");
                if (double.TryParse(Console.ReadLine(), out double radius) && radius > 0.0)
                {
                    shapes.Add(new Circle(radius));
                }
                else
                {
                    Console.WriteLine("Radius must be positive.");
                }
            }
            else if (option == "2")
            {
                Console.Write("Width: ");
                bool validWidth = double.TryParse(Console.ReadLine(), out double width);
                Console.Write("Height: ");
                bool validHeight = double.TryParse(Console.ReadLine(), out double height);

                if (validWidth && validHeight && width > 0.0 && height > 0.0)
                {
                    shapes.Add(new Rectangle(width, height));
                }
                else
                {
                    Console.WriteLine("Width and height must be positive.");
                }
            }
            else if (option == "3")
            {
                if (shapes.Count == 0)
                {
                    Console.WriteLine("No shapes added yet.");
                    continue;
                }

                double totalArea = 0.0;
                foreach (Shape shape in shapes)
                {
                    double shapeArea = shape.Area();
                    totalArea += shapeArea;
                    Console.WriteLine($"- {shape.Name()} area: {shapeArea}");
                }
                Console.WriteLine($"Total area: {totalArea}");
            }
            else if (option == "4")
            {
                Console.WriteLine("Goodbye.");
                return;
            }
            else
            {
                Console.WriteLine("Invalid option.");
            }
        }
    }
}
