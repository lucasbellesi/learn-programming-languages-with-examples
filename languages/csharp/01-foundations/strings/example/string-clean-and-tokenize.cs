// This helper example focuses on isolating string cleanup before the main example combines the steps.

// This extra example extends strings with text normalization and token extraction.

using System;
using System.Collections.Generic;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
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
