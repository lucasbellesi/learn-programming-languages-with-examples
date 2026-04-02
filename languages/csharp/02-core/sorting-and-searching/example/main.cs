// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: practicing sorting and searching patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for sorting and searching; this keeps the walkthrough readable.
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

    // Walk through one fixed scenario so sorting and searching behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key sorting and searching path.
        List<int> values = new List<int> { 7, 2, 9, 4, 2, 8 };
        values.Sort();

        // Report values so learners can verify the sorting and searching outcome.
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
