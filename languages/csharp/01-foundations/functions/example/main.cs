// This example shows breaking behavior into reusable functions with clear inputs and outputs.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

    // Run one deterministic scenario so the console output makes breaking behavior into reusable functions with clear inputs and outputs easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine(Add(4, 6));

        int[] numbers = { 10, 20, 30 };
        PrintArray(numbers);
        SwapInArray(numbers, 0, 1);
        PrintArray(numbers);
    }
}
