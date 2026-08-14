using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter integers separated by spaces: ");
        string line = Console.ReadLine() ?? "";

        if (string.IsNullOrWhiteSpace(line))
        {
            Console.WriteLine("No values entered.");
            return;
        }

        List<int> values = new List<int>();
        foreach (string token in line.Split(' ', StringSplitOptions.RemoveEmptyEntries))
        {
            values.Add(int.Parse(token));
        }

        Console.Write("Target value: ");
        int target = int.Parse(Console.ReadLine() ?? "0");

        int frequency = 0;
        foreach (int value in values)
        {
            if (value == target)
            {
                frequency++;
            }
        }

        Console.WriteLine($"Frequency of {target}: {frequency}");
    }
}
