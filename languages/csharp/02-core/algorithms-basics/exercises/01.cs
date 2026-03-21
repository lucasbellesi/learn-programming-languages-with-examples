using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many integers? ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        if (n <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        List<int> values = new List<int>();
        for (int i = 0; i < n; i++)
        {
            Console.Write($"Value {i + 1}: ");
            values.Add(int.Parse(Console.ReadLine() ?? "0"));
        }

        Console.Write("Target to find: ");
        int target = int.Parse(Console.ReadLine() ?? "0");

        int firstIndex = -1;
        for (int i = 0; i < values.Count; i++)
        {
            if (values[i] == target)
            {
                firstIndex = i;
                break;
            }
        }

        Console.WriteLine($"First index: {firstIndex}");
    }
}
