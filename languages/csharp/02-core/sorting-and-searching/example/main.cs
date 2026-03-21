// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Collections.Generic;

class Program
{
    static int BinarySearch(List<int> values, int target)
    {
        int left = 0;
        int right = values.Count - 1;

        // Intent: narrow the search window deterministically based on sorted order.
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int midValue = values[mid];

            // Intent: return immediately when the exact match is found.
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

    static void Main()
    {
        // Program flow: sort values first, then search on the sorted collection.
        List<int> values = new List<int> { 7, 2, 9, 4, 2, 8 };
        values.Sort();

        // Intent: print sorted data so learners can verify search preconditions.
        Console.WriteLine($"Sorted: {string.Join(" ", values)}");

        int target = 4;
        int index = BinarySearch(values, target);

        // Intent: guard the not-found case explicitly instead of assuming success.
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
