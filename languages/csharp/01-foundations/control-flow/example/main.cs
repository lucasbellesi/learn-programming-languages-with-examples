// This example demonstrates control flow concepts.

using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter an integer: ");
        int value = int.Parse(Console.ReadLine() ?? "0");

        if (value > 0)
        {
            Console.WriteLine("positive");
        }
        else if (value < 0)
        {
            Console.WriteLine("negative");
        }
        else
        {
            Console.WriteLine("zero");
        }

        Console.Write("Enter N: ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        int factorial = 1;
        for (int i = 1; i <= n; i++)
        {
            factorial *= i;
        }

        Console.WriteLine($"factorial({n}) = {factorial}");
        Console.WriteLine("Numbers 1..N:");
        for (int i = 1; i <= n; i++)
        {
            Console.WriteLine(i);
        }
    }
}
