// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: the example makes it possible to implement linear scans and accumulations with
// clear invariants before the learner tackles the exercises.

using System;
using System.Collections.Generic;

class Program
{
    // Fixed inputs make the consequence of forgetting empty-collection checks before min/max
    // logic visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        List<int> values = new List<int> { 4, 7, 4, 1, 9, 4, 2 };
        int target = 4;

        int firstIndex = AlgorithmTools.LinearSearch(values, target);
        // The printed result shows whether the program can analyze behavior for empty, duplicate,
        // and missing values.
        Console.WriteLine($"First index of {target}: {firstIndex}");
        Console.WriteLine(
            $"Occurrences of {target}: {AlgorithmTools.CountOccurrences(values, target)}"
        );

        if (!AlgorithmTools.TryGetMinMax(values, out int minValue, out int maxValue))
        {
            Console.WriteLine("No values to process.");
            return;
        }

        Console.WriteLine($"Minimum: {minValue}");
        Console.WriteLine($"Maximum: {maxValue}");
    }
}
