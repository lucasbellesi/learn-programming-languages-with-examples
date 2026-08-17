using System;

internal static class Program
{
    private static void RunMemoryManagementRaiiExercise()
    {
        string? depthText = Console.ReadLine();
        // TODO 1: Validate depthText as a positive number of nested scopes.
        // TODO 2: Scope guard that proves nested cleanup order.
        // TODO 3: Produce enter/exit logs proving automatic cleanup; verify nested scopes; final active
        //         counter must return to zero.
        _ = depthText;
    }

    private static void Main()
    {
        RunMemoryManagementRaiiExercise();
    }
}
