// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: the example makes it possible to reject malformed and out-of-domain input
// without corrupting state before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to reject malformed and out-of-domain input
// without corrupting state.
class Program
{
    static int ReadIntInRange(string prompt, int minValue, int maxValue)
    {
        while (true)
        {
            Console.Write(prompt);
            string? raw = Console.ReadLine();
            // Parse first, then validate the numeric range before returning.
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
            // The same validation shape works for decimal input too.
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

    // Fixed inputs make the consequence of using `int.Parse` or `double.Parse` directly for
    // user-entered text visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // Only validated values reach the final summary.
        int age = ReadIntInRange("Enter your age (1-120): ", 1, 120);
        double gpa = ReadDoubleInRange("Enter your GPA (0.0-4.0): ", 0.0, 4.0);

        // The printed result shows whether the program can design retry and termination behavior
        // that cannot loop accidentally.
        Console.WriteLine();
        Console.WriteLine("Validated input summary:");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
    }
}
