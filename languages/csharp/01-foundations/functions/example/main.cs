// This example demonstrates functions concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

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
        // Intent: print intermediate or final output for quick behavior verification.
        Console.WriteLine("[" + string.Join(", ", values) + "]");
    }

    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        Console.WriteLine(Add(4, 6));

        int[] numbers = { 10, 20, 30 };
        PrintArray(numbers);
        SwapInArray(numbers, 0, 1);
        PrintArray(numbers);
    }
}
