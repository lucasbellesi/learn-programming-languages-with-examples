// This example shows combining values through expressions and readable calculations.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes combining values through expressions and readable calculations easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
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
