// Module focus: How copying, sharing, or transferring state changes later behavior.
// Why it matters: practicing copy and move semantics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for copy and move semantics; this keeps the walkthrough readable.
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
    // Walk through one fixed scenario so copy and move semantics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key copy and move semantics path.
        Buffer first = new Buffer(3);
        Buffer second = first.Clone();
        Buffer third = second.Transfer();

        // Report values so learners can verify the copy and move semantics outcome.
        Console.WriteLine($"first size: {first.Size}");
        Console.WriteLine($"second size (after transfer): {second.Size}");
        Console.WriteLine($"third size: {third.Size}");
    }
}
