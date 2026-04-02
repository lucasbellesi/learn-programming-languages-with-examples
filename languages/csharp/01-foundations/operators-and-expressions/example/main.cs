// Module focus: Combining values through expressions and readable calculations.
// Why it matters: practicing operators and expressions patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for operators and expressions; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so operators and expressions behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key operators and expressions path.
        // Report values so learners can verify the operators and expressions outcome.
        Console.Write("Enter total seconds: ");
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
