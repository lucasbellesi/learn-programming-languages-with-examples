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

    public void ExpireForDemo(string key)
    {
        if (entries.TryGetValue(key, out WeakReference<CachedValue>? reference))
        {
            reference.SetTarget(null!);
        }
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
        string scenario = Console.ReadLine() ?? "missing";
        WeakCache cache = new WeakCache();
        if (scenario == "missing")
        {
            cache.PrintLookup("entry");
            return;
        }

        CachedValue value = new CachedValue("payload");
        cache.Store("entry", value);
        if (scenario == "expired")
        {
            cache.ExpireForDemo("entry");
        }
        cache.PrintLookup("entry");
        GC.KeepAlive(value);
    }
}
