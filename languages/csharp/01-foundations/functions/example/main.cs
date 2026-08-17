// Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
// Why it matters: the example makes it possible to decompose a problem into focused functions
// with explicit contracts before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to decompose a problem into focused
// functions with explicit contracts.
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

    // Fixed inputs make the consequence of embedding all logic in main instead of reusable
    // helpers visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can use parameters and return values
        // without hidden state changes.
        Console.WriteLine(Add(4, 6));

        int[] numbers = { 10, 20, 30 };
        PrintArray(numbers);
        SwapInArray(numbers, 0, 1);
        PrintArray(numbers);
    }
}
