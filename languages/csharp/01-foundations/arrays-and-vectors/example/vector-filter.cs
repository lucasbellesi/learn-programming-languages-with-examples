// This extra example extends arrays-and-vectors with a focused filtering task.
// Example purpose: isolate list building and threshold-based filtering.

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many numbers? ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        List<int> values = new List<int>(count);
        for (int index = 0; index < count; index++)
        {
            Console.Write($"Value {index + 1}: ");
            if (!int.TryParse(Console.ReadLine(), out int value))
            {
                Console.WriteLine("Please enter valid integers only.");
                return;
            }

            values.Add(value);
        }

        Console.Write("Filter values greater than or equal to: ");
        if (!int.TryParse(Console.ReadLine(), out int threshold))
        {
            Console.WriteLine("Please enter a valid threshold.");
            return;
        }

        List<int> filtered = values.FindAll(value => value >= threshold);
        if (filtered.Count > 0)
        {
            Console.WriteLine("Filtered values: " + string.Join(", ", filtered));
        }
        else
        {
            Console.WriteLine("Filtered values: none");
        }
    }
}
