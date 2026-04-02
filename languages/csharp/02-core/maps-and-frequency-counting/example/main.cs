// This example shows counting repeated values and summarizing them through keyed lookups.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes counting repeated values and summarizing them through keyed lookups easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        string text = "banana bandana";
        SortedDictionary<char, int> frequencies = new SortedDictionary<char, int>();

        foreach (char ch in text)
        {
            if (ch == ' ')
            {
                continue;
            }

            if (!frequencies.ContainsKey(ch))
            {
                frequencies[ch] = 0;
            }

            frequencies[ch]++;
        }

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine("Character frequencies:");
        foreach (KeyValuePair<char, int> entry in frequencies)
        {
            Console.WriteLine($"{entry.Key} -> {entry.Value}");
        }
    }
}
