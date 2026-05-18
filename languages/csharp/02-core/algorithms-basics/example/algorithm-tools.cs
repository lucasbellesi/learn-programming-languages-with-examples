// Module focus: Keep small algorithms isolated so each loop has one job.
// Why it matters: named helper methods make search, counting, and scans easier to test.

using System.Collections.Generic;

static class AlgorithmTools
{
    public static int LinearSearch(List<int> values, int target)
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

    public static int CountOccurrences(List<int> values, int target)
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

    public static bool TryGetMinMax(List<int> values, out int minValue, out int maxValue)
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
}
