// Example purpose: compare a couple of small optimization choices with Stopwatch.

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

class Program
{
    static void Main()
    {
        // Program flow: measure two paired implementations on the same workload size.
        const int lineCount = 4000;
        long concatTicks = Measure(() => BuildWithConcatenation(lineCount));
        long builderTicks = Measure(() => BuildWithStringBuilder(lineCount));

        Console.WriteLine($"String concatenation ticks: {concatTicks}");
        Console.WriteLine($"StringBuilder ticks: {builderTicks}");

        const int itemCount = 200000;
        long noCapacityTicks = Measure(() => FillWithoutCapacity(itemCount));
        long withCapacityTicks = Measure(() => FillWithCapacity(itemCount));

        // Intent: final output keeps the comparison direct and easy to verify.
        Console.WriteLine($"List fill without capacity ticks: {noCapacityTicks}");
        Console.WriteLine($"List fill with capacity ticks: {withCapacityTicks}");
    }

    static long Measure(Action action)
    {
        Stopwatch stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        return stopwatch.ElapsedTicks;
    }

    static string BuildWithConcatenation(int lineCount)
    {
        string result = string.Empty;
        for (int index = 0; index < lineCount; index++)
        {
            result += $"row-{index};";
        }

        return result;
    }

    static string BuildWithStringBuilder(int lineCount)
    {
        StringBuilder builder = new StringBuilder(lineCount * 8);
        for (int index = 0; index < lineCount; index++)
        {
            builder.Append("row-");
            builder.Append(index);
            builder.Append(';');
        }

        return builder.ToString();
    }

    static List<int> FillWithoutCapacity(int itemCount)
    {
        List<int> values = new List<int>();
        for (int index = 0; index < itemCount; index++)
        {
            values.Add(index);
        }

        return values;
    }

    static List<int> FillWithCapacity(int itemCount)
    {
        List<int> values = new List<int>(itemCount);
        for (int index = 0; index < itemCount; index++)
        {
            values.Add(index);
        }

        return values;
    }
}
