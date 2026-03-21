using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter numeric values separated by spaces: ");
        string line = Console.ReadLine() ?? "";

        if (string.IsNullOrWhiteSpace(line))
        {
            Console.WriteLine("No values entered.");
            return;
        }

        var values = new List<double>();
        foreach (string token in line.Split(' ', StringSplitOptions.RemoveEmptyEntries))
        {
            values.Add(double.Parse(token));
        }

        Console.Write("Decimal precision (0-6): ");
        int precision = int.Parse(Console.ReadLine() ?? "2");

        if (precision < 0 || precision > 6)
        {
            Console.WriteLine("Precision must be between 0 and 6.");
            return;
        }

        double sum = 0;
        double min = values[0];
        double max = values[0];

        foreach (double value in values)
        {
            sum += value;
            if (value < min) min = value;
            if (value > max) max = value;
        }

        double average = sum / values.Count;
        string format = "F" + precision;

        Console.WriteLine($"Count: {values.Count}");
        Console.WriteLine($"Sum: {sum.ToString(format)}");
        Console.WriteLine($"Average: {average.ToString(format)}");
        Console.WriteLine($"Minimum: {min.ToString(format)}");
        Console.WriteLine($"Maximum: {max.ToString(format)}");
    }
}
