using System;

sealed class ScopeGuard : IDisposable
{
    private readonly string label;
    private bool disposed;
    private static int activeCount;

    public ScopeGuard(string label)
    {
        this.label = label;
        activeCount++;
        Console.WriteLine($"enter {label} (active={activeCount})");
    }

    public static int ActiveCount => activeCount;

    public void Dispose()
    {
        if (disposed)
        {
            return;
        }

        disposed = true;
        activeCount--;
        Console.WriteLine($"exit {label} (active={activeCount})");
        GC.SuppressFinalize(this);
    }
}

class Program
{
    static void Main()
    {
        Console.WriteLine($"Active before scopes: {ScopeGuard.ActiveCount}");

        using (new ScopeGuard("outer"))
        {
            Console.WriteLine($"Active inside outer: {ScopeGuard.ActiveCount}");

            using (new ScopeGuard("inner"))
            {
                Console.WriteLine($"Active inside inner: {ScopeGuard.ActiveCount}");
            }

            Console.WriteLine($"Active after inner: {ScopeGuard.ActiveCount}");
        }

        Console.WriteLine($"Active after scopes: {ScopeGuard.ActiveCount}");
    }
}
