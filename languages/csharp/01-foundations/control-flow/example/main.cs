// This example shows choosing between branches and repeating work with predictable control flow.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes choosing between branches and repeating work with predictable control flow easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
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
