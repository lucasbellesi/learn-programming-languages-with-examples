using System;
using System.Collections.Generic;
using System.Diagnostics;

class Program
{
    static void Main()
    {
        Console.Write("Element count: ");
        if (!int.TryParse(Console.ReadLine(), out int elementCount))
        {
            Console.WriteLine("Invalid element count.");
            return;
        }

        if (elementCount < 0)
        {
            Console.WriteLine("Element count cannot be negative.");
            return;
        }

        long noCapacityTicks = Measure(() => FillWithoutCapacity(elementCount));
        long withCapacityTicks = Measure(() => FillWithCapacity(elementCount));

        Console.WriteLine($"Without capacity ticks: {noCapacityTicks}");
        Console.WriteLine($"With capacity ticks: {withCapacityTicks}");
    }

    static long Measure(Action action)
    {
        Stopwatch stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        return stopwatch.ElapsedTicks;
    }

    static List<int> FillWithoutCapacity(int elementCount)
    {
        List<int> values = new List<int>();
        for (int index = 0; index < elementCount; index++)
        {
            values.Add(index);
        }

        return values;
    }

    static List<int> FillWithCapacity(int elementCount)
    {
        List<int> values = new List<int>(elementCount);
        for (int index = 0; index < elementCount; index++)
        {
            values.Add(index);
        }

        return values;
    }
}
