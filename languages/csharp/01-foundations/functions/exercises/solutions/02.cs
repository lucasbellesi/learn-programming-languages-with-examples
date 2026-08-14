using System;

class Program
{
    static int CountVowels(string text)
    {
        string vowels = "aeiou";
        int count = 0;

        foreach (char ch in text.ToLowerInvariant())
        {
            if (vowels.Contains(ch))
            {
                count++;
            }
        }

        return count;
    }

    static void Main()
    {
        Console.Write("Enter text: ");
        string line = Console.ReadLine() ?? "";

        Console.WriteLine($"Number of vowels: {CountVowels(line)}");
    }
}
