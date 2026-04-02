// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: practicing input validation patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for input validation; this keeps the walkthrough readable.
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

    // Walk through one fixed scenario so input validation behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key input validation path.
        int age = ReadIntInRange("Enter your age (1-120): ", 1, 120);
        double gpa = ReadDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

        // Report values so learners can verify the input validation outcome.
        Console.WriteLine();
        Console.WriteLine("Validated input summary:");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
    }
}
