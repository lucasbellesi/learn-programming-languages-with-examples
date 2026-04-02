// This helper example focuses on isolating one collection transformation so the filtering rule stands out.

// This extra example extends arrays-and-vectors with a focused filtering task.

using System;
using System.Collections.Generic;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
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
