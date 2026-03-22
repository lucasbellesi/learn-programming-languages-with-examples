// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Collections.Generic;

class Buffer
{
    private List<int> values;

    public Buffer(int size)
    {
        // Intent: normalize invalid sizes so state stays predictable.
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
        // Intent: deep copy isolates future changes between instances.
        Buffer copy = new Buffer(new List<int>(values));
        Console.WriteLine("Cloned");
        return copy;
    }

    public Buffer Transfer()
    {
        // Intent: transfer operation moves internal ownership-like responsibility.
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
    static void Main()
    {
        // Program flow: create, clone, transfer, then inspect resulting states.
        Buffer first = new Buffer(3);
        Buffer second = first.Clone();
        Buffer third = second.Transfer();

        Console.WriteLine($"first size: {first.Size}");
        Console.WriteLine($"second size (after transfer): {second.Size}");
        Console.WriteLine($"third size: {third.Size}");
    }
}
