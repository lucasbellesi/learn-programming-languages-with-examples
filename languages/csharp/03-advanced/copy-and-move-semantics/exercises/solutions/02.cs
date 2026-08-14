using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many strings? ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        List<string> values = new List<string>(count);

        for (int i = 0; i < count; i++)
        {
            Console.Write($"String {i + 1}: ");
            string input = Console.ReadLine() ?? string.Empty;
            values.Add(input);

            List<string> alias = values;
            List<string> snapshot = new List<string>(values);

            Console.WriteLine($"Current size: {values.Count}");
            Console.WriteLine($"Alias sees size: {alias.Count}");
            Console.WriteLine($"Snapshot size: {snapshot.Count}");
        }
    }
}
