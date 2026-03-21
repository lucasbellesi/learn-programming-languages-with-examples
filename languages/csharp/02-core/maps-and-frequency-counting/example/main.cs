// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Program flow: iterate input text, count symbols, then print a frequency table.
        string text = "banana bandana";
        SortedDictionary<char, int> frequencies = new SortedDictionary<char, int>();

        // Intent: process characters in a deterministic sequence from the source text.
        foreach (char ch in text)
        {
            // Intent: skip separators so counts represent meaningful symbols.
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

        // Intent: print final frequency results in sorted key order.
        Console.WriteLine("Character frequencies:");
        foreach (KeyValuePair<char, int> entry in frequencies)
        {
            Console.WriteLine($"{entry.Key} -> {entry.Value}");
        }
    }
}
