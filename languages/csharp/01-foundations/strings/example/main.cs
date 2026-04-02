// Module focus: Cleaning and combining text while preserving readable string logic.
// Why it matters: practicing strings patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Text;

// Helper setup for strings; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so strings behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key strings path.
        // Report values so learners can verify the strings outcome.
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
