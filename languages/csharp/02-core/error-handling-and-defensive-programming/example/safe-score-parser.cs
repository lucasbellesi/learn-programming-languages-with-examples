// This extra example extends defensive programming with safe score parsing.
// Example purpose: reject malformed or out-of-range rows without stopping the program.

using System;
using System.Collections.Generic;

class Program
{
    static bool TryParseRow(string row, out string name, out int score)
    {
        name = string.Empty;
        score = 0;

        string[] parts = row.Split(':');
        if (parts.Length != 2)
        {
            return false;
        }

        name = parts[0].Trim();
        if (name.Length == 0)
        {
            return false;
        }

        if (!int.TryParse(parts[1].Trim(), out score))
        {
            return false;
        }

        return score >= 0 && score <= 100;
    }

    static void Main()
    {
        string[] rows =
        {
            "Ana: 91",
            "InvalidRow",
            "Bruno: not-a-number",
            "Carla: 77",
            "Diego: 130",
        };
        List<(string Name, int Score)> validRows = new List<(string Name, int Score)>();

        foreach (string row in rows)
        {
            if (!TryParseRow(row, out string name, out int score))
            {
                Console.WriteLine($"Skipping invalid row: {row}");
                continue;
            }

            validRows.Add((name, score));
        }

        Console.WriteLine($"Valid rows: {validRows.Count}");
        foreach ((string name, int score) in validRows)
        {
            Console.WriteLine($"- {name} => {score}");
        }
    }
}
