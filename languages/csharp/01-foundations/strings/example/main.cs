// This example shows cleaning and combining text while preserving readable string logic.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Text;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Program
{
    // Run one deterministic scenario so the console output makes cleaning and combining text while preserving readable string logic easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
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
