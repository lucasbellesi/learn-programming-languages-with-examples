using System;

internal static class Program
{
    private static void RunSmartPointersInDepthExercise()
    {
        string scenario = Console.ReadLine() ?? "missing";
        // TODO 1: Accept `alive`, `expired`, or `missing` as the lookup scenario.
        // TODO 2: Observe cache entries through `WeakReference<T>`.
        // TODO 3: Produce alive/expired cache lookup logs; verify expired weak reference; cache miss.
        _ = scenario;
    }

    private static void Main()
    {
        RunSmartPointersInDepthExercise();
    }
}
