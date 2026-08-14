using System;

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
                Console.WriteLine("Invalid input. Please enter an integer.");
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
                Console.WriteLine("Invalid input. Please enter a number.");
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
        int count = ReadIntInRange("How many scores (1-50)? ", 1, 50);

        double total = 0.0;
        for (int i = 0; i < count; i++)
        {
            double score = ReadDoubleInRange($"Score {i + 1} (0-100): ", 0.0, 100.0);
            total += score;
        }

        Console.WriteLine($"Average score: {total / count:F2}");
    }
}
