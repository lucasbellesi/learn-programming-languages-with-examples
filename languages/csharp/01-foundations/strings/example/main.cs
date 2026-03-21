using System;
using System.Text;

class Program
{
    static void Main()
    {
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
