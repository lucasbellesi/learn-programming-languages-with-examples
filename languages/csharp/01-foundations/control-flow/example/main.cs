// Module focus: Choosing between branches and repeating work with predictable control flow.
// Why it matters: the example makes it possible to select branches that cover normal and boundary
// conditions before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to select branches that cover normal and
// boundary conditions.
class Program
{
    // Fixed inputs make the consequence of not handling non-positive upper bounds before entering
    // loops visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can write terminating loops and reason
        // about their invariants.
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
