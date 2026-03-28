using System;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.Write("Enter two numbers to divide (a b): ");
            string raw = Console.ReadLine() ?? string.Empty;
            string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

            if (
                parts.Length != 2
                || !double.TryParse(parts[0], out double a)
                || !double.TryParse(parts[1], out double b)
            )
            {
                Console.WriteLine("Invalid input type. Try again.");
                continue;
            }

            if (b == 0.0)
            {
                Console.WriteLine("Divisor cannot be zero. Try again.");
                continue;
            }

            Console.WriteLine($"Result: {a / b}");
            break;
        }
    }
}
