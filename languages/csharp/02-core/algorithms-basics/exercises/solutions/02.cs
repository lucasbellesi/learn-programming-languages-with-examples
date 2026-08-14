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

        int minValue = values[0];
        int maxValue = values[0];
        int evenCount = 0;

        foreach (int value in values)
        {
            if (value < minValue)
            {
                minValue = value;
            }
            if (value > maxValue)
            {
                maxValue = value;
            }
            if (value % 2 == 0)
            {
                evenCount++;
            }
        }

        Console.WriteLine($"Minimum: {minValue}");
        Console.WriteLine($"Maximum: {maxValue}");
        Console.WriteLine($"Even numbers: {evenCount}");
    }
}
