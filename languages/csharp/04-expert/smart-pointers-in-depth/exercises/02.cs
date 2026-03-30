using System;
using System.Collections.Generic;

sealed class CachedValue
{
    public CachedValue(string text)
    {
        Text = text;
    }

    public string Text { get; }
}

sealed class WeakCache
{
    private readonly Dictionary<string, WeakReference<CachedValue>> entries =
        new Dictionary<string, WeakReference<CachedValue>>();

    public void Store(string key, CachedValue value)
    {
        entries[key] = new WeakReference<CachedValue>(value);
    }

    public void PrintLookup(string key)
    {
        if (!entries.TryGetValue(key, out WeakReference<CachedValue>? reference))
        {
            Console.WriteLine($"{key}: missing");
            return;
        }

        if (reference.TryGetTarget(out CachedValue? value))
        {
            Console.WriteLine($"{key}: alive -> {value.Text}");
            return;
        }

        Console.WriteLine($"{key}: expired");
    }
}

class Program
{
    static void Main()
    {
        WeakCache cache = new WeakCache();
        cache.Store("stable", new CachedValue("Still referenced"));

        CachedValue temporary = new CachedValue("Short lived");
        cache.Store("temp", temporary);
        cache.PrintLookup("stable");
        cache.PrintLookup("temp");

        temporary = null!;
        GC.Collect();
        GC.WaitForPendingFinalizers();
        GC.Collect();

        cache.PrintLookup("stable");
        cache.PrintLookup("temp");
        cache.PrintLookup("missing");
    }
}
