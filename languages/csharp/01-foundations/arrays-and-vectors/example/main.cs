// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: practicing arrays and vectors patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for arrays and vectors; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so arrays and vectors behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key arrays and vectors path.
        int[] fixedScores = { 72, 88, 95 };
        // Report values so learners can verify the arrays and vectors outcome.
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
