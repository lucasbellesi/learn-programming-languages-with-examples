// Module focus: Walking data step by step to compute summaries and decisions.
// Why it matters: practicing algorithms basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for algorithms basics; this keeps the walkthrough readable.
class Program
{
    static int LinearSearch(List<int> values, int target)
    {
        for (int index = 0; index < values.Count; index++)
        {
            if (values[index] == target)
            {
                return index;
            }
        }

        return -1;
    }

    static int CountOccurrences(List<int> values, int target)
    {
        int count = 0;
        foreach (int value in values)
        {
            if (value == target)
            {
                count++;
            }
        }

        return count;
    }

    static bool TryGetMinMax(List<int> values, out int minValue, out int maxValue)
    {
        minValue = 0;
        maxValue = 0;

        if (values.Count == 0)
        {
            return false;
        }

        minValue = values[0];
        maxValue = values[0];

        foreach (int value in values)
        {
            if (value < minValue)
            {
                minValue = value;
            }

            if (value > maxValue)
            {
                maxValue = value;
            }
        }

        return true;
    }

    // Walk through one fixed scenario so algorithms basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key algorithms basics path.
        List<int> values = new List<int> { 4, 7, 4, 1, 9, 4, 2 };
        int target = 4;

        int firstIndex = LinearSearch(values, target);
        // Report values so learners can verify the algorithms basics outcome.
        Console.WriteLine($"First index of {target}: {firstIndex}");
        Console.WriteLine($"Occurrences of {target}: {CountOccurrences(values, target)}");

        if (!TryGetMinMax(values, out int minValue, out int maxValue))
        {
            Console.WriteLine("No values to process.");
            return;
        }

        Console.WriteLine($"Minimum: {minValue}");
        Console.WriteLine($"Maximum: {maxValue}");
    }
}
