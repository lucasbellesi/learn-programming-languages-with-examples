// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: practicing performance and profiling basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;

// Helper setup for performance and profiling basics; this keeps the walkthrough readable.
class Program
{
    static string retainedText = string.Empty;
    static List<int> retainedValues = new List<int>();

    // Walk through two fixed comparisons so the timing output stays repeatable.
    static void Main()
    {
        // First compare string building strategies on the same workload.
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

        // Report values so learners can verify the performance and profiling basics outcome.
        Console.WriteLine(
            $"Average string concatenation ticks ({repetitions} runs): {concatTicks}"
        );
        Console.WriteLine($"Average StringBuilder ticks ({repetitions} runs): {builderTicks}");

        // Then compare list growth with and without pre-allocated capacity.
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
        // Warm up once so setup and JIT effects are less likely to dominate the average.
        action();

        // Time the exact same action repeatedly because one run can be noisy.
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
        // Repeated string concatenation allocates new strings as the result grows.
        string result = string.Empty;
        for (int index = 0; index < lineCount; index++)
        {
            result += $"row-{index};";
        }

        return result;
    }

    static string BuildWithStringBuilder(int lineCount)
    {
        // StringBuilder keeps one growing buffer, which usually reduces allocation pressure.
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
        // This version lets the list resize itself as more items are appended.
        List<int> values = new List<int>();
        for (int index = 0; index < itemCount; index++)
        {
            values.Add(index);
        }

        return values;
    }

    static List<int> FillWithCapacity(int itemCount)
    {
        // This version reserves enough space up front for the known workload size.
        List<int> values = new List<int>(itemCount);
        for (int index = 0; index < itemCount; index++)
        {
            values.Add(index);
        }

        return values;
    }
}
