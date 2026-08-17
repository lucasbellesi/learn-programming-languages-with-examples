// Module focus: Writing generic code that stays useful across multiple data types.
// Why it matters: the example makes it possible to express reusable type-safe behavior with
// language generics before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to express reusable type-safe behavior with
// language generics.
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
    // Fixed inputs make the consequence of assuming all generic types support comparison
    // automatically visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can apply constraints when an operation
        // requires specific capabilities.
        Console.WriteLine($"MaxValue(4, 7) = {Helpers.MaxValue(4, 7)}");
        Console.WriteLine($"MaxValue(2.5, 1.2) = {Helpers.MaxValue(2.5, 1.2)}");

        Pair<string> pair = new Pair<string>("left", "right");
        pair.Print();
    }
}
