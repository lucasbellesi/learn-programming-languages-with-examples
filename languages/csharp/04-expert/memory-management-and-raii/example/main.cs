// This example shows tying resource cleanup to object lifetime so cleanup stays predictable.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
sealed class BufferLease : IDisposable
{
    private int[]? values;
    private readonly string name;
    private bool disposed;
    private static int activeLeases;

    public BufferLease(string name, int length)
    {
        this.name = name;
        values = new int[length];
        activeLeases++;
        Console.WriteLine($"[acquire] {name} length={length} active={activeLeases}");
    }

    public static int ActiveLeases => activeLeases;

    public void FillSequence(int start, int step)
    {
        EnsureNotDisposed();

        for (int i = 0; i < values!.Length; i++)
        {
            values[i] = start + (i * step);
        }
    }

    public int Sum()
    {
        EnsureNotDisposed();

        int total = 0;
        foreach (int value in values!)
        {
            total += value;
        }

        return total;
    }

    public string Describe()
    {
        EnsureNotDisposed();
        return string.Join(" ", values!);
    }

    public void Dispose()
    {
        if (disposed)
        {
            return;
        }

        disposed = true;
        values = null;
        activeLeases--;
        Console.WriteLine($"[dispose] {name} active={activeLeases}");
        GC.SuppressFinalize(this);
    }

    ~BufferLease()
    {
        if (!disposed)
        {
            activeLeases--;
            Console.WriteLine($"[finalizer] {name} active={activeLeases}");
        }
    }

    private void EnsureNotDisposed()
    {
        if (disposed)
        {
            throw new ObjectDisposedException(name);
        }
    }
}

class Program
{
    // Run one deterministic scenario so the console output makes tying resource cleanup to object lifetime so cleanup stays predictable easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"Active leases before scope: {BufferLease.ActiveLeases}");

        using (BufferLease scores = new BufferLease("scores", 5))
        {
            int threshold = 25;
            scores.FillSequence(10, 5);

            Console.WriteLine($"Scores: {scores.Describe()}");
            Console.WriteLine($"Sum: {scores.Sum()}");
            Console.WriteLine($"Threshold for review: {threshold}");

            using BufferLease scratch = new BufferLease("scratch", 3);
            scratch.FillSequence(1, 1);
            Console.WriteLine($"Scratch buffer: {scratch.Describe()}");
            Console.WriteLine($"Active leases inside scope: {BufferLease.ActiveLeases}");
        }

        Console.WriteLine($"Active leases after scope: {BufferLease.ActiveLeases}");
    }
}
