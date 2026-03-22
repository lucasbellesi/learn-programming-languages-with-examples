using System;
using System.Collections.Generic;

static class Helpers
{
    public static double AverageOf<T>(IReadOnlyList<T> values) where T : IConvertible
    {
        if (values.Count == 0)
        {
            return 0.0;
        }

        double sum = 0.0;
        foreach (T value in values)
        {
            sum += value.ToDouble(System.Globalization.CultureInfo.InvariantCulture);
        }

        return sum / values.Count;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("How many numbers? ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count < 0)
        {
            Console.WriteLine("Please enter zero or a positive count.");
            return;
        }

        List<double> values = new List<double>(count);
        for (int index = 0; index < count; index++)
        {
            string rawValue = Console.ReadLine() ?? string.Empty;
            if (!double.TryParse(rawValue, out double parsed))
            {
                Console.WriteLine("Invalid number.");
                return;
            }

            values.Add(parsed);
        }

        Console.WriteLine($"Average: {Helpers.AverageOf(values)}");
    }
}
