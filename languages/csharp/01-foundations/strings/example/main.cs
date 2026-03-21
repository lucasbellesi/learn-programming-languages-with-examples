// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.Text;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        // Intent: print intermediate or final output for quick behavior verification.
        Console.Write("Enter a sentence: ");
        // Intent: gather typed input first so later operations are predictable.
        string line = Console.ReadLine() ?? "";

        StringBuilder cleanedBuilder = new StringBuilder();
        // Intent: iterate through data in a clear and deterministic order.
        foreach (char ch in line)
        {
            // Intent: guard invalid or edge-case paths before the main path continues.
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
