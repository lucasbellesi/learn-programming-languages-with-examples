using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("Enter integers (-1 to stop):");
        List<int> values = new List<int>();

        while (true)
        {
            int current = int.Parse(Console.ReadLine() ?? "-1");
            if (current == -1)
            {
                break;
            }
            values.Add(current);
        }

        if (values.Count == 0)
        {
            Console.WriteLine("No values entered.");
            return;
        }

        int sum = 0;
        foreach (int value in values)
        {
            sum += value;
        }

        Console.WriteLine($"Average: {(double)sum / values.Count:F4}");
    }
}
