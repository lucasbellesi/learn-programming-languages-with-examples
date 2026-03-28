// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

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
        // Intent: print final state from a generic container in one predictable format.
        Console.WriteLine($"({first}, {second})");
    }
}

class Program
{
    static void Main()
    {
        // Program flow: call one generic method, then inspect one generic class instance.
        Console.WriteLine($"MaxValue(4, 7) = {Helpers.MaxValue(4, 7)}");
        Console.WriteLine($"MaxValue(2.5, 1.2) = {Helpers.MaxValue(2.5, 1.2)}");

        Pair<string> pair = new Pair<string>("left", "right");
        pair.Print();
    }
}
