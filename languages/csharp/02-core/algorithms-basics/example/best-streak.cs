// This extra example extends algorithms basics with a best-streak scan.
// Example purpose: track the longest rising streak with one pass.

using System;
using System.Collections.Generic;

class Program
{
    static List<int> LongestRisingStreak(List<int> values)
    {
        if (values.Count == 0)
        {
            return new List<int>();
        }

        int bestLength = 1;
        int bestStart = 0;
        int currentLength = 1;
        int currentStart = 0;

        for (int index = 1; index < values.Count; index++)
        {
            if (values[index] > values[index - 1])
            {
                currentLength++;
            }
            else
            {
                currentLength = 1;
                currentStart = index;
            }

            if (currentLength > bestLength)
            {
                bestLength = currentLength;
                bestStart = currentStart;
            }
        }

        return values.GetRange(bestStart, bestLength);
    }

    static void Main()
    {
        List<int> temperatures = new List<int> { 17, 18, 21, 19, 20, 22, 25, 24 };
        List<int> streak = LongestRisingStreak(temperatures);

        Console.WriteLine($"Longest rising streak length: {streak.Count}");
        Console.WriteLine($"Streak values: [{string.Join(", ", streak)}]");
    }
}
