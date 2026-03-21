using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many values? ");
        int count = int.Parse(Console.ReadLine() ?? "0");

        if (count <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        List<int> values = new List<int>();
        for (int i = 0; i < count; i++)
        {
            Console.Write($"Value {i + 1}: ");
            values.Add(int.Parse(Console.ReadLine() ?? "0"));
        }

        Console.WriteLine("Values in reverse order:");
        for (int i = values.Count - 1; i >= 0; i--)
        {
            Console.WriteLine(values[i]);
        }
    }
}
