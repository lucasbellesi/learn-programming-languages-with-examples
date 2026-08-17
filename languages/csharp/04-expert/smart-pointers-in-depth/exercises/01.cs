using System;

internal static class Program
{
    private static void RunSmartPointersInDepthExercise()
    {
        string sourceName = Console.ReadLine() ?? "empty";
        string destinationName = Console.ReadLine() ?? "empty";
        // TODO 1: Convert `empty` to a null holder and other lines to owned documents.
        // TODO 2: Move an owned document reference between holders.
        // TODO 3: Produce ownership transfer logs before and after moving; verify moving from an empty
        //         owner; destination already holding another object.
        _ = sourceName;
        _ = destinationName;
    }

    private static void Main()
    {
        RunSmartPointersInDepthExercise();
    }
}
