using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        int[] fixedScores = { 72, 88, 95 };
        Console.WriteLine($"Fixed array values: {string.Join(", ", fixedScores)}");

        Console.Write("How many temperatures do you want to enter? ");
        int count = int.Parse(Console.ReadLine() ?? "0");

        if (count <= 0)
        {
            Console.WriteLine("Nothing to process.");
            return;
        }

        List<double> temperatures = new List<double>();
        for (int i = 0; i < count; i++)
        {
            Console.Write($"Temperature {i + 1}: ");
            temperatures.Add(double.Parse(Console.ReadLine() ?? "0"));
        }

        double sum = 0;
        foreach (double value in temperatures)
        {
            sum += value;
        }

        Console.WriteLine($"Average temperature: {sum / temperatures.Count:F2}");
    }
}
