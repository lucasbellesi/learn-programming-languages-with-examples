// This example shows measuring hot paths before changing code for speed.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    static string retainedText = string.Empty;
    static List<int> retainedValues = new List<int>();

    // Run one deterministic scenario so the console output makes measuring hot paths before changing code for speed easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        const int lineCount = 4000;
        const int repetitions = 12;
        long concatTicks = MeasureAverage(
            () => retainedText = BuildWithConcatenation(lineCount),
            repetitions
        );
        long builderTicks = MeasureAverage(
            () => retainedText = BuildWithStringBuilder(lineCount),
            repetitions
        );

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine(
            $"Average string concatenation ticks ({repetitions} runs): {concatTicks}"
        );
        Console.WriteLine($"Average StringBuilder ticks ({repetitions} runs): {builderTicks}");

        const int itemCount = 200000;
        long noCapacityTicks = MeasureAverage(
            () => retainedValues = FillWithoutCapacity(itemCount),
            repetitions
        );
        long withCapacityTicks = MeasureAverage(
            () => retainedValues = FillWithCapacity(itemCount),
            repetitions
        );

        Console.WriteLine(
            $"Average list fill without capacity ticks ({repetitions} runs): {noCapacityTicks}"
        );
        Console.WriteLine(
            $"Average list fill with capacity ticks ({repetitions} runs): {withCapacityTicks}"
        );
    }

    static long MeasureAverage(Action action, int repetitions)
    {
        action();

        long totalTicks = 0;
        for (int iteration = 0; iteration < repetitions; iteration++)
        {
            Stopwatch stopwatch = Stopwatch.StartNew();
            action();
            stopwatch.Stop();
            totalTicks += stopwatch.ElapsedTicks;
        }

        return totalTicks / repetitions;
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
