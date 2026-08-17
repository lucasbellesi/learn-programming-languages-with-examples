// Module focus: Storing related values in ordered collections and iterating safely.
// Why it matters: the example makes it possible to store and traverse ordered collections safely
// before the learner tackles the exercises.

using System;
using System.Collections.Generic;

// Separate helpers keep the main path focused on how to store and traverse ordered collections
// safely.
class Program
{
    // Fixed inputs make the consequence of trusting collection size input when count is zero or
    // negative visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        int[] fixedScores = { 72, 88, 95 };
        // The printed result shows whether the program can handle empty collections and index
        // boundaries explicitly.
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
