// Module focus: Reordering data and locating values with deliberate search logic.
// Why it matters: the example makes it possible to choose and apply sorting and searching
// operations correctly before the learner tackles the exercises.

using System;
using System.Collections.Generic;

// Separate helpers keep the main path focused on how to choose and apply sorting and searching
// operations correctly.
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

    // Fixed inputs make the consequence of running binary search on unsorted input visible and
    // repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        List<int> values = new List<int> { 7, 2, 9, 4, 2, 8 };
        values.Sort();

        // The printed result shows whether the program can explain ordering, duplicates, missing
        // values, and stability tradeoffs.
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
