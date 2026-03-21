// This example demonstrates control flow concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        // Intent: print intermediate or final output for quick behavior verification.
        Console.Write("Enter an integer: ");
        // Intent: gather typed input first so later operations are predictable.
        int value = int.Parse(Console.ReadLine() ?? "0");

        // Intent: guard invalid or edge-case paths before the main path continues.
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
        // Intent: iterate through data in a clear and deterministic order.
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
