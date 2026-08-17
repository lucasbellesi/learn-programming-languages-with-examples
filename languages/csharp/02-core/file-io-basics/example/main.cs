// Module focus: Reading plain-text files, parsing rows, and writing clear results.
// Why it matters: the example makes it possible to read and write explicit paths while reporting
// I/O failures before the learner tackles the exercises.

using System;
using System.IO;

// Separate helpers keep the main path focused on how to read and write explicit paths while
// reporting I/O failures.
class Program
{
    static bool TryParseScoreRow(string line, out string name, out int score)
    {
        name = string.Empty;
        score = 0;

        // Each valid row has one name token followed by one integer score.
        string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length != 2 || !int.TryParse(parts[1], out score))
        {
            return false;
        }

        name = parts[0];
        return true;
    }

    // Fixed inputs make the consequence of assuming input files always exist visible and
    // repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        string inputPath = Path.Combine(Path.GetTempPath(), "learn-lang-file-io-csharp-scores.txt");
        string outputPath = Path.Combine(
            Path.GetTempPath(),
            "learn-lang-file-io-csharp-summary.txt"
        );
        File.WriteAllLines(inputPath, new[] { "ana 90", "bob 82", "invalid row", "carla 95" });

        int validRows = 0;
        int sum = 0;

        // Read one row at a time so malformed rows can be skipped safely.
        foreach (string line in File.ReadLines(inputPath))
        {
            if (!TryParseScoreRow(line, out string name, out int score))
            {
                continue;
            }

            validRows++;
            sum += score;
            // The printed result shows whether the program can parse records defensively and
            // distinguish valid from rejected rows.
            Console.WriteLine($"{name} -> {score}");
        }

        double average = (double)sum / validRows;

        // Persist the summary separately from the console walkthrough.
        File.WriteAllLines(outputPath, new[] { $"Rows: {validRows}", $"Average: {average:F2}" });
        Console.WriteLine($"Summary written to {outputPath}");
    }
}
