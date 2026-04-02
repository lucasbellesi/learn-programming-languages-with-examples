// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: practicing functions patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for functions; this keeps the walkthrough readable.
class Program
{
    static int Add(int a, int b)
    {
        return a + b;
    }

    static void SwapInArray(int[] values, int i, int j)
    {
        int temp = values[i];
        values[i] = values[j];
        values[j] = temp;
    }

    static void PrintArray(int[] values)
    {
        Console.WriteLine("[" + string.Join(", ", values) + "]");
    }

    // Walk through one fixed scenario so functions behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key functions path.
        // Report values so learners can verify the functions outcome.
        Console.WriteLine(Add(4, 6));

        int[] numbers = { 10, 20, 30 };
        PrintArray(numbers);
        SwapInArray(numbers, 0, 1);
        PrintArray(numbers);
    }
}
