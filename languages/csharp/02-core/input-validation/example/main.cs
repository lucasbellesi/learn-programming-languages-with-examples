// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static int ReadIntInRange(string prompt, int minValue, int maxValue)
    {
        // Intent: iterate through data in a clear and deterministic order.
        while (true)
        {
            // Intent: print intermediate or final output for quick behavior verification.
            Console.Write(prompt);
            // Intent: gather typed input first so later operations are predictable.
            string? raw = Console.ReadLine();
            // Intent: guard invalid or edge-case paths before the main path continues.
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

    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        int age = ReadIntInRange("Enter your age (1-120): ", 1, 120);
        double gpa = ReadDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

        Console.WriteLine();
        Console.WriteLine("Validated input summary:");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
    }
}
