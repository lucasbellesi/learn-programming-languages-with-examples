// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: the example makes it possible to predict aliasing and independence after
// copying or sharing values before the learner tackles the exercises.

using System;
using System.Collections.Generic;

// Separate helpers keep the main path focused on how to predict aliasing and independence after
// copying or sharing values.
class Buffer
{
    private List<int> values;

    public Buffer(int size)
    {
        int safeSize = size < 0 ? 0 : size;
        values = new List<int>(new int[safeSize]);
        Console.WriteLine($"Constructed (size={values.Count})");
    }

    private Buffer(List<int> sourceValues)
    {
        values = sourceValues;
    }

    public Buffer Clone()
    {
        Buffer copy = new Buffer(new List<int>(values));
        Console.WriteLine("Cloned");
        return copy;
    }

    public Buffer Transfer()
    {
        List<int> movedValues = values;
        values = new List<int>();
        Buffer transferred = new Buffer(movedValues);
        Console.WriteLine($"Transferred (size={transferred.Size})");
        return transferred;
    }

    public int Size => values.Count;
}

class Program
{
    // Fixed inputs make the consequence of assuming assignment duplicates object contents for
    // classes visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        Buffer first = new Buffer(3);
        Buffer second = first.Clone();
        Buffer third = second.Transfer();

        // The printed result shows whether the program can choose an idiomatic ownership-transfer
        // strategy for the language.
        Console.WriteLine($"first size: {first.Size}");
        Console.WriteLine($"second size (after transfer): {second.Size}");
        Console.WriteLine($"third size: {third.Size}");
    }
}
