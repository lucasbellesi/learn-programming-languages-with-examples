using System;

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

        int total = 0;
        for (int i = 0; i < count; i++)
        {
            Console.Write($"Value {i + 1}: ");
            int value = int.Parse(Console.ReadLine() ?? "0");
            total += value;
        }

        Console.WriteLine($"Sum: {total}");
        Console.WriteLine($"Average: {(double)total / count:F2}");
    }
}
