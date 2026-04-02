// This helper example focuses on focusing on the frequency summary without repeating the full program flow.

// This extra example extends maps-and-frequency-counting with ranked frequency output.

using System;
using System.Collections.Generic;
using System.Linq;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Program
{
    static void Main()
    {
        Console.Write("How many words? ");
        if (!int.TryParse(Console.ReadLine(), out int count) || count <= 0)
        {
            Console.WriteLine("Please enter a positive number.");
            return;
        }

        Dictionary<string, int> frequency = new Dictionary<string, int>();
        for (int index = 0; index < count; index++)
        {
            Console.Write($"Word {index + 1}: ");
            string word = (Console.ReadLine() ?? string.Empty).Trim();
            frequency[word] = frequency.GetValueOrDefault(word) + 1;
        }

        Console.Write("How many top words to show? ");
        if (!int.TryParse(Console.ReadLine(), out int k) || k <= 0)
        {
            Console.WriteLine("Please enter a positive value for k.");
            return;
        }

        List<KeyValuePair<string, int>> items = frequency
            .OrderByDescending(entry => entry.Value)
            .ThenBy(entry => entry.Key)
            .Take(k)
            .ToList();

        Console.WriteLine($"\nTop {items.Count} words:");
        for (int index = 0; index < items.Count; index++)
        {
            Console.WriteLine($"{index + 1}. {items[index].Key} -> {items[index].Value}");
        }
    }
}
