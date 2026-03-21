// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        int[] fixedScores = { 72, 88, 95 };
        // Intent: print intermediate or final output for quick behavior verification.
        Console.WriteLine($"Fixed array values: {string.Join(", ", fixedScores)}");

        Console.Write("How many temperatures do you want to enter? ");
        // Intent: gather typed input first so later operations are predictable.
        int count = int.Parse(Console.ReadLine() ?? "0");

        // Intent: guard invalid or edge-case paths before the main path continues.
        if (count <= 0)
        {
            Console.WriteLine("Nothing to process.");
            return;
        }

        List<double> temperatures = new List<double>();
        // Intent: iterate through data in a clear and deterministic order.
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
