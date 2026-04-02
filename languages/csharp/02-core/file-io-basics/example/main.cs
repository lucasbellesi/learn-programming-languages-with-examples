// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: practicing file io basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.IO;

// Helper setup for file io basics; this keeps the walkthrough readable.
class Program
{
    static bool TryParseScoreRow(string line, out string name, out int score)
    {
        name = string.Empty;
        score = 0;

        string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length != 2 || !int.TryParse(parts[1], out score))
        {
            return false;
        }

        name = parts[0];
        return true;
    }

    // Walk through one fixed scenario so file io basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key file io basics path.
        string runDirectory = Path.Combine(Path.GetTempPath(), "learn-lang-file-io-csharp");
        Directory.CreateDirectory(runDirectory);
        string inputPath = Path.Combine(runDirectory, "scores.txt");
        string outputPath = Path.Combine(runDirectory, "summary.txt");

        if (!File.Exists(inputPath))
        {
            File.WriteAllLines(inputPath, new[] { "ana 90", "bob 82", "invalid row", "carla 95" });
        }

        int validRows = 0;
        int sum = 0;

        using (StreamReader reader = new StreamReader(inputPath))
        {
            string? line;
            while ((line = reader.ReadLine()) is not null)
            {
                if (!TryParseScoreRow(line, out string name, out int score))
                {
                    continue;
                }

                validRows++;
                sum += score;
                // Report values so learners can verify the file io basics outcome.
                Console.WriteLine($"{name} -> {score}");
            }
        }

        if (validRows == 0)
        {
            Console.WriteLine("No valid rows found.");
            return;
        }

        double average = (double)sum / validRows;

        using (StreamWriter writer = new StreamWriter(outputPath, false))
        {
            writer.WriteLine($"Rows: {validRows}");
            writer.WriteLine($"Average: {average:F2}");
        }

        Console.WriteLine($"Summary written to {outputPath}");
    }
}
