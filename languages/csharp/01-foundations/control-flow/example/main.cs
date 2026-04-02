// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for control flow; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so control flow behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key control flow path.
        // Report values so learners can verify the control flow outcome.
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
