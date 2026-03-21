using System;

readonly struct Rectangle
{
    public Rectangle(double width, double height)
    {
        Width = width;
        Height = height;
    }

    public double Width { get; }
    public double Height { get; }

    public double Area()
    {
        return Width * Height;
    }

    public double Perimeter()
    {
        return 2.0 * (Width + Height);
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter width and height: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (parts.Length != 2 ||
            !double.TryParse(parts[0], out double width) ||
            !double.TryParse(parts[1], out double height))
        {
            Console.WriteLine("Invalid input. Enter exactly two numbers.");
            return;
        }

        if (width <= 0.0 || height <= 0.0)
        {
            Console.WriteLine("Width and height must be positive.");
            return;
        }

        Rectangle rectangle = new Rectangle(width, height);
        Console.WriteLine($"Area: {rectangle.Area()}");
        Console.WriteLine($"Perimeter: {rectangle.Perimeter()}");
    }
}
