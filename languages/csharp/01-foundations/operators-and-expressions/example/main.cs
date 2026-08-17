// Module focus: Combining values through expressions and readable calculations.
// Why it matters: the example makes it possible to build expressions with correct precedence and
// explicit intent before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to build expressions with correct precedence
// and explicit intent.
class Program
{
    // Fixed inputs make the consequence of forgetting to reject negative totals for time
    // conversion or subtotal visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can distinguish arithmetic, comparison,
        // and logical operations.
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
