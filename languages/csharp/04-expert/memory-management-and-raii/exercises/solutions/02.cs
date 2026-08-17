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
        if (!int.TryParse(Console.ReadLine(), out int depth) || depth <= 0)
        {
            Console.WriteLine("Depth must be positive.");
            return;
        }

        Console.WriteLine($"Active before scopes: {ScopeGuard.ActiveCount}");
        RunNestedScopes(depth, 1);
        Console.WriteLine($"Active after scopes: {ScopeGuard.ActiveCount}");
    }

    static void RunNestedScopes(int depth, int level)
    {
        if (level > depth)
        {
            Console.WriteLine($"Active at deepest scope: {ScopeGuard.ActiveCount}");
            return;
        }

        using ScopeGuard guard = new ScopeGuard($"scope-{level}");
        RunNestedScopes(depth, level + 1);
    }
}
