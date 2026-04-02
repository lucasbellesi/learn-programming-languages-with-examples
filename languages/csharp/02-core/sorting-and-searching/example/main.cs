// This example shows reordering data and locating values with deliberate search logic.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    static int BinarySearch(List<int> values, int target)
    {
        int left = 0;
        int right = values.Count - 1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int midValue = values[mid];

            if (midValue == target)
            {
                return mid;
            }

            if (midValue < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        return -1;
    }

    // Run one deterministic scenario so the console output makes reordering data and locating values with deliberate search logic easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        List<int> values = new List<int> { 7, 2, 9, 4, 2, 8 };
        values.Sort();

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"Sorted: {string.Join(" ", values)}");

        int target = 4;
        int index = BinarySearch(values, target);

        if (index >= 0)
        {
            Console.WriteLine($"Found {target} at index {index}");
        }
        else
        {
            Console.WriteLine($"{target} not found");
        }
    }
}
