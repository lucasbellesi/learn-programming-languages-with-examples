// Module focus: Measuring hot paths before changing code for speed.
// Why it matters: the example makes it possible to measure before optimizing and interpret timing
// data cautiously before the learner tackles the exercises.

using System;
using System.Diagnostics;
using System.Text;

// Separate helpers keep the main path focused on how to measure before optimizing and interpret
// timing data cautiously.
class Program
{
    const int Repetitions = 12;

    // Walk through two fixed comparisons so the timing output stays repeatable.
    static void Main()
    {
        // First compare string building strategies on the same workload.
        const int lineCount = 4000;
        // The printed result shows whether the program can relate algorithmic and allocation
        // choices to observed cost.
        Report("Average string concatenation ticks", () => BuildText(lineCount, false));
        Report("Average StringBuilder ticks", () => BuildText(lineCount, true));

        // Then measure list growth with pre-allocated capacity.
        const int itemCount = 200000;
        Report("Average list fill with capacity ticks", () => FillValues(itemCount));
    }

    static void Report(string label, Func<object> action)
    {
        Console.WriteLine($"{label} ({Repetitions} runs): {MeasureAverage(action)}");
    }

    static long MeasureAverage(Func<object> action)
    {
        // Warm up once so setup and JIT effects are less likely to dominate the average.
        GC.KeepAlive(action());

        // Time the exact same action repeatedly because one run can be noisy.
        long totalTicks = 0;
        for (int iteration = 0; iteration < Repetitions; iteration++)
        {
            Stopwatch stopwatch = Stopwatch.StartNew();
            GC.KeepAlive(action());
            stopwatch.Stop();
            totalTicks += stopwatch.ElapsedTicks;
        }

        return totalTicks / Repetitions;
    }

    static string BuildText(int lineCount, bool useBuilder)
    {
        // Compare repeated concatenation with a reusable StringBuilder buffer.
        if (useBuilder)
        {
            StringBuilder builder = new StringBuilder(lineCount * 8);
            for (int index = 0; index < lineCount; index++)
            {
                builder.Append("row-").Append(index).Append(';');
            }

            return builder.ToString();
        }

        string result = string.Empty;
        for (int index = 0; index < lineCount; index++)
        {
            result += $"row-{index};";
        }

        return result;
    }

    static int[] FillValues(int itemCount)
    {
        // Reserving capacity avoids repeated backing-array growth.
        int[] values = new int[itemCount];
        for (int index = 0; index < itemCount; index++)
        {
            values[index] = index;
        }

        return values;
    }
}
