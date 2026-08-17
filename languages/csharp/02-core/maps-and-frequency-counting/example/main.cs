// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: the example makes it possible to use key-value collections to aggregate and
// retrieve data before the learner tackles the exercises.

using System;
using System.Collections.Generic;

// Separate helpers keep the main path focused on how to use key-value collections to aggregate
// and retrieve data.
class Program
{
    // Fixed inputs make the consequence of assuming missing keys exist before initialization
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
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

        // The printed result shows whether the program can define normalization and missing-key
        // behavior explicitly.
        Console.WriteLine("Character frequencies:");
        foreach (KeyValuePair<char, int> entry in frequencies)
        {
            Console.WriteLine($"{entry.Key} -> {entry.Value}");
        }
    }
}
