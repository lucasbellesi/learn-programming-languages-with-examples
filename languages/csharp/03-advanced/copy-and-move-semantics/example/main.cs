// This example shows how copying, sharing, or transferring state changes later behavior.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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
    // Run one deterministic scenario so the console output makes how copying, sharing, or transferring state changes later behavior easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        Buffer first = new Buffer(3);
        Buffer second = first.Clone();
        Buffer third = second.Transfer();

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"first size: {first.Size}");
        Console.WriteLine($"second size (after transfer): {second.Size}");
        Console.WriteLine($"third size: {third.Size}");
    }
}
