// This example shows reading plain-text files, parsing rows, and writing clear results.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.IO;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

    // Run one deterministic scenario so the console output makes reading plain-text files, parsing rows, and writing clear results easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
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
                // Print the observed state here so learners can connect the code path to a concrete result.
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
