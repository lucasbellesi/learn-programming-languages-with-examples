// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;
using System.IO;

class Program
{
    static bool TryParseScoreRow(string line, out string name, out int score)
    {
        name = string.Empty;
        score = 0;

        // Intent: normalize row parsing so the main flow can stay focused on I/O steps.
        string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        // Intent: guard malformed rows before numeric parsing logic runs.
        if (parts.Length != 2 || !int.TryParse(parts[1], out score))
        {
            return false;
        }

        name = parts[0];
        return true;
    }

    static void Main()
    {
        // Program flow: prepare input, parse rows, then generate a summary file.
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
            // Intent: iterate through file rows in a deterministic order.
            while ((line = reader.ReadLine()) is not null)
            {
                if (!TryParseScoreRow(line, out string name, out int score))
                {
                    continue;
                }

                validRows++;
                sum += score;
                // Intent: print parsed rows so learners can verify intermediate state.
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
