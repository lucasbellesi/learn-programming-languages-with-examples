// This extra example extends templates-basics with reusable typed helpers.
// Example purpose: print sequences and sum numeric values with one shared implementation.

using System;
using System.Collections.Generic;
using System.Numerics;

class Program
{
    static void PrintList<T>(IReadOnlyList<T> values, string label)
    {
        Console.Write($"{label}: [");
        for (int index = 0; index < values.Count; index++)
        {
            if (index > 0)
            {
                Console.Write(", ");
            }
            Console.Write(values[index]);
        }
        Console.WriteLine("]");
    }

    static T SumList<T>(IEnumerable<T> values)
        where T : INumber<T>
    {
        T total = T.Zero;
        foreach (T value in values)
        {
            total += value;
        }
        return total;
    }

    static void Main()
    {
        List<int> numbers = new List<int> { 2, 4, 6, 8 };
        List<double> prices = new List<double> { 1.5, 2.25, 3.75 };

        PrintList(numbers, "Numbers");
        PrintList(prices, "Prices");

        Console.WriteLine($"Sum of numbers: {SumList(numbers)}");
        Console.WriteLine($"Sum of prices: {SumList(prices)}");
    }
}
