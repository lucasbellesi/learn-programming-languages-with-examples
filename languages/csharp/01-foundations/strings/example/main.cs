// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: the example makes it possible to normalize, inspect, and transform textual data
// before the learner tackles the exercises.

using System;
using System.Text;

// Separate helpers keep the main path focused on how to normalize, inspect, and transform textual
// data.
class Program
{
    // Fixed inputs make the consequence of counting words without removing extra spaces visible
    // and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can handle empty input and character
        // boundaries safely.
        Console.Write("Enter a sentence: ");
        string line = Console.ReadLine() ?? "";

        StringBuilder cleanedBuilder = new StringBuilder();
        foreach (char ch in line)
        {
            if (char.IsLetterOrDigit(ch))
            {
                cleanedBuilder.Append(char.ToLowerInvariant(ch));
            }
            else
            {
                cleanedBuilder.Append(' ');
            }
        }

        string cleaned = cleanedBuilder.ToString();
        string[] words = cleaned.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        Console.WriteLine($"Normalized text: {cleaned}");
        Console.WriteLine($"Tokens ({words.Length}):");
        foreach (string word in words)
        {
            Console.WriteLine($"- {word}");
        }
    }
}
