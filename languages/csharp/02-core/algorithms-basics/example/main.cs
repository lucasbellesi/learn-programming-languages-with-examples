// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

class Program
{
    // Walk through one fixed scenario so algorithms basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key algorithms basics path.
        List<int> values = new List<int> { 4, 7, 4, 1, 9, 4, 2 };
        int target = 4;

        int firstIndex = AlgorithmTools.LinearSearch(values, target);
        // Report values so learners can verify the algorithms basics outcome.
        Console.WriteLine($"First index of {target}: {firstIndex}");
        Console.WriteLine($"Occurrences of {target}: {AlgorithmTools.CountOccurrences(values, target)}");

        if (!AlgorithmTools.TryGetMinMax(values, out int minValue, out int maxValue))
        {
            Console.WriteLine("No values to process.");
            return;
        }

        Console.WriteLine($"Minimum: {minValue}");
        Console.WriteLine($"Maximum: {maxValue}");
    }
}
