// This extra example extends strings with text normalization and token extraction.
// Example purpose: separate character cleanup from token building.

using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter a sentence: ");
        string line = Console.ReadLine() ?? string.Empty;

        char[] cleanedChars = new char[line.Length];
        for (int index = 0; index < line.Length; index++)
        {
            char current = line[index];
            cleanedChars[index] = char.IsLetterOrDigit(current)
                ? char.ToLowerInvariant(current)
                : ' ';
        }

        string cleaned = new string(cleanedChars);
        List<string> words = new List<string>(
            cleaned.Split(' ', StringSplitOptions.RemoveEmptyEntries)
        );

        Console.WriteLine($"Normalized text: {cleaned}");
        Console.WriteLine($"Tokens ({words.Count}):");
        foreach (string word in words)
        {
            Console.WriteLine($"- {word}");
        }
    }
}
