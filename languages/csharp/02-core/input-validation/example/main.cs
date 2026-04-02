// This example shows rejecting invalid input before the main workflow continues.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    static int ReadIntInRange(string prompt, int minValue, int maxValue)
    {
        while (true)
        {
            Console.Write(prompt);
            string? raw = Console.ReadLine();
            if (!int.TryParse(raw, out int value))
            {
                Console.WriteLine("Invalid input type. Please enter an integer.");
                continue;
            }

            if (value < minValue || value > maxValue)
            {
                Console.WriteLine($"Value must be between {minValue} and {maxValue}.");
                continue;
            }

            return value;
        }
    }

    static double ReadDoubleInRange(string prompt, double minValue, double maxValue)
    {
        while (true)
        {
            Console.Write(prompt);
            string? raw = Console.ReadLine();
            if (!double.TryParse(raw, out double value))
            {
                Console.WriteLine("Invalid input type. Please enter a decimal number.");
                continue;
            }

            if (value < minValue || value > maxValue)
            {
                Console.WriteLine($"Value must be between {minValue:F1} and {maxValue:F1}.");
                continue;
            }

            return value;
        }
    }

    // Run one deterministic scenario so the console output makes rejecting invalid input before the main workflow continues easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        int age = ReadIntInRange("Enter your age (1-120): ", 1, 120);
        double gpa = ReadDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine();
        Console.WriteLine("Validated input summary:");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
    }
}
