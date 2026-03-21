using System;

abstract class Shape
{
    public abstract double Area();
}

class Triangle : Shape
{
    private readonly double @base;
    private readonly double height;

    public Triangle(double baseValue, double heightValue)
    {
        @base = baseValue;
        height = heightValue;
    }

    public override double Area()
    {
        return 0.5 * @base * height;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter base and height: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (parts.Length != 2 ||
            !double.TryParse(parts[0], out double baseValue) ||
            !double.TryParse(parts[1], out double heightValue))
        {
            Console.WriteLine("Invalid input.");
            return;
        }

        Triangle triangle = new Triangle(baseValue, heightValue);
        Console.WriteLine($"Triangle area: {triangle.Area()}");
    }
}
