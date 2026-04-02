// This helper example focuses on isolating the parsing guard so invalid text never silently becomes a score.

// This extra example extends defensive programming with safe score parsing.

using System;
using System.Collections.Generic;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
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
