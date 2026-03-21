// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        // Intent: print intermediate or final output for quick behavior verification.
        Console.Write("Enter total seconds: ");
        // Intent: gather typed input first so later operations are predictable.
        int totalSeconds = int.Parse(Console.ReadLine() ?? "0");

        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;

        Console.WriteLine($"Time: {hours}:{minutes:D2}:{seconds:D2}");

        Console.Write("Enter first number: ");
        double a = double.Parse(Console.ReadLine() ?? "0");
        Console.Write("Enter second number: ");
        double b = double.Parse(Console.ReadLine() ?? "0");

        Console.WriteLine($"Sum: {a + b:F4}");
        Console.WriteLine($"Difference: {a - b:F4}");
        Console.WriteLine($"Product: {a * b:F4}");

        // Intent: guard invalid or edge-case paths before the main path continues.
        if (b != 0)
        {
            Console.WriteLine($"Division: {a / b:F4}");
        }
        else
        {
            Console.WriteLine("Division is not possible because second number is zero.");
        }
    }
}
