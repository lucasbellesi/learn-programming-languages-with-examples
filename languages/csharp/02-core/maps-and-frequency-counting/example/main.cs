// Module focus: Counting repeated values and summarizing them through keyed lookups.
// Why it matters: practicing maps and frequency counting patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

// Helper setup for maps and frequency counting; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so maps and frequency counting behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key maps and frequency counting path.
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

        // Report values so learners can verify the maps and frequency counting outcome.
        Console.WriteLine("Character frequencies:");
        foreach (KeyValuePair<char, int> entry in frequencies)
        {
            Console.WriteLine($"{entry.Key} -> {entry.Value}");
        }
    }
}
