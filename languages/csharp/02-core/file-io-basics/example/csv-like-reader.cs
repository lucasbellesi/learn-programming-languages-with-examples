// This helper example focuses on separating row parsing from the higher-level file workflow.

// This extra example extends file-io-basics with line parsing and validation.

using System;
using System.Collections.Generic;
using System.IO;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class StudentScore
{
    public string Name { get; init; } = string.Empty;

    public int Score { get; init; }
}

class Program
{
    static void Main()
    {
        Console.Write("CSV-like input file path (name,score): ");
        string path = (Console.ReadLine() ?? string.Empty).Trim();

        if (!File.Exists(path))
        {
            Console.WriteLine($"Could not open file: {path}");
            return;
        }

        List<StudentScore> rows = new List<StudentScore>();
        string[] lines = File.ReadAllLines(path);

        for (int index = 0; index < lines.Length; index++)
        {
            string line = lines[index].Trim();
            if (line.Length == 0)
            {
                continue;
            }

            string[] parts = line.Split(',', 2);
            if (parts.Length != 2)
            {
                Console.WriteLine($"Skipping malformed line {index + 1}: {line}");
                continue;
            }

            if (!int.TryParse(parts[1], out int score) || score < 0 || score > 100)
            {
                Console.WriteLine($"Skipping invalid score on line {index + 1}: {parts[1]}");
                continue;
            }

            rows.Add(new StudentScore { Name = parts[0], Score = score });
        }

        Console.WriteLine($"\nValid rows: {rows.Count}");
        foreach (StudentScore row in rows)
        {
            Console.WriteLine($"- {row.Name}: {row.Score}");
        }
    }
}
