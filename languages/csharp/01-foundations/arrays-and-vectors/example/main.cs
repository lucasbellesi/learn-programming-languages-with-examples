// This example shows storing related values in ordered collections and iterating safely.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes storing related values in ordered collections and iterating safely easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        int[] fixedScores = { 72, 88, 95 };
        // Print the observed state here so learners can connect the code path to a concrete result.
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
