// Module focus: Tying resource cleanup to object lifetime so cleanup stays predictable.
// Why it matters: practicing memory management and raii patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for memory management and raii; this keeps the walkthrough readable.
sealed class BufferLease : IDisposable
{
    private int[] values;
    private readonly string name;
    private bool disposed;
    private static int activeLeases;

    public BufferLease(string name, int length)
    {
        // Acquiring the lease simulates taking ownership of a resource.
        this.name = name;
        values = new int[length];
        activeLeases++;
        Console.WriteLine($"[acquire] {name} length={length} active={activeLeases}");
    }

    public static int ActiveLeases => activeLeases;

    public void FillSequence(int start, int step)
    {
        for (int i = 0; i < values!.Length; i++)
        {
            values[i] = start + (i * step);
        }
    }

    public string Describe() => string.Join(" ", values);

    public void Dispose()
    {
        // Dispose may be called more than once, so cleanup must be idempotent.
        if (disposed)
        {
            return;
        }

        disposed = true;
        values = Array.Empty<int>();
        activeLeases--;
        Console.WriteLine($"[dispose] {name} active={activeLeases}");
        GC.SuppressFinalize(this);
    }
}

class Program
{
    // Walk through one fixed scope so resource lifetime is easy to inspect.
    static void Main()
    {
        // Start outside the ownership scope so learners can see the baseline count.
        Console.WriteLine($"Active leases before scope: {BufferLease.ActiveLeases}");

        // The using block calls Dispose automatically when the scope exits.
        using (BufferLease scores = new BufferLease("scores", 5))
        {
            scores.FillSequence(10, 5);

            // Report buffer state while the lease is still valid.
            Console.WriteLine($"Scores: {scores.Describe()}");
            Console.WriteLine($"Active leases inside scope: {BufferLease.ActiveLeases}");
        }

        // After scope exit, both leases have been disposed and the count returns to zero.
        Console.WriteLine($"Active leases after scope: {BufferLease.ActiveLeases}");
    }
}
