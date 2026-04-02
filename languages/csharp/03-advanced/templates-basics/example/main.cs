// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: practicing templates basics patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for templates basics; this keeps the walkthrough readable.
static class Helpers
{
    public static T MaxValue<T>(T left, T right)
        where T : IComparable<T>
    {
        return left.CompareTo(right) > 0 ? left : right;
    }
}

class Pair<T>
{
    private readonly T first;
    private readonly T second;

    public Pair(T firstValue, T secondValue)
    {
        first = firstValue;
        second = secondValue;
    }

    public void Print()
    {
        Console.WriteLine($"({first}, {second})");
    }
}

class Program
{
    // Walk through one fixed scenario so templates basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key templates basics path.
        // Report values so learners can verify the templates basics outcome.
        Console.WriteLine($"MaxValue(4, 7) = {Helpers.MaxValue(4, 7)}");
        Console.WriteLine($"MaxValue(2.5, 1.2) = {Helpers.MaxValue(2.5, 1.2)}");

        Pair<string> pair = new Pair<string>("left", "right");
        pair.Print();
    }
}
