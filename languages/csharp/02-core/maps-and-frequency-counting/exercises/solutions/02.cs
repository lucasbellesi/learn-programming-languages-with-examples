using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("Enter text: ");
        string text = Console.ReadLine() ?? string.Empty;

        Dictionary<char, int> frequency = new Dictionary<char, int>();
        foreach (char ch in text)
        {
            if (!frequency.ContainsKey(ch))
            {
                frequency[ch] = 0;
            }

            frequency[ch]++;
        }

        char result = '\0';
        foreach (char ch in text)
        {
            if (frequency[ch] == 1)
            {
                result = ch;
                break;
            }
        }

        if (result == '\0')
        {
            Console.WriteLine("No non-repeating character found.");
        }
        else
        {
            Console.WriteLine($"First non-repeating character: {result}");
        }
    }
}
