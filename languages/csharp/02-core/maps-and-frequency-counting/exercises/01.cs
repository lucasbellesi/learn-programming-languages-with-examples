using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many digits? ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        if (n <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        Dictionary<int, int> frequency = new Dictionary<int, int>();
        for (int digit = 0; digit <= 9; digit++)
        {
            frequency[digit] = 0;
        }

        for (int i = 0; i < n; i++)
        {
            int value = int.Parse(Console.ReadLine() ?? "0");
            if (value >= 0 && value <= 9)
            {
                frequency[value]++;
            }
        }

        for (int digit = 0; digit <= 9; digit++)
        {
            Console.WriteLine($"{digit} -> {frequency[digit]}");
        }
    }
}
