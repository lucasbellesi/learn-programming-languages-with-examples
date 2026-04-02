// This example shows writing generic code that stays useful across multiple data types.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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
    // Run one deterministic scenario so the console output makes writing generic code that stays useful across multiple data types easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"MaxValue(4, 7) = {Helpers.MaxValue(4, 7)}");
        Console.WriteLine($"MaxValue(2.5, 1.2) = {Helpers.MaxValue(2.5, 1.2)}");

        Pair<string> pair = new Pair<string>("left", "right");
        pair.Print();
    }
}
