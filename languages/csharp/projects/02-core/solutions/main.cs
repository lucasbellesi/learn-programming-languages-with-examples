using System;
using System.Globalization;
using System.IO;

class Program
{
    static bool TryParseRow(string line, out string name, out int score)
    {
        name = string.Empty;
        score = 0;

        string[] parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length < 2)
        {
            return false;
        }

        if (!int.TryParse(parts[^1], out score))
        {
            return false;
        }

        name = string.Join(" ", parts, 0, parts.Length - 1);
        return name.Length > 0;
    }

    static void Main()
    {
        Console.Write("Enter input file path: ");
        string inputPath = Console.ReadLine() ?? string.Empty;

        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Could not open input file.");
            return;
        }

        int validRows = 0;
        int invalidRows = 0;
        int minScore = 0;
        int maxScore = 0;
        int sum = 0;

        foreach (string rawLine in File.ReadLines(inputPath))
        {
            if (!TryParseRow(rawLine, out _, out int score))
            {
                invalidRows++;
                continue;
            }

            if (validRows == 0)
            {
                minScore = score;
                maxScore = score;
            }
            else
            {
                if (score < minScore)
                {
                    minScore = score;
                }
                if (score > maxScore)
                {
                    maxScore = score;
                }
            }

            sum += score;
            validRows++;
        }

        using StreamWriter report = new StreamWriter("report.txt");
        report.WriteLine($"Valid rows: {validRows}");
        report.WriteLine($"Invalid rows: {invalidRows}");

        if (validRows > 0)
        {
            double average = (double)sum / validRows;
            report.WriteLine($"Average: {average.ToString(CultureInfo.InvariantCulture)}");
            report.WriteLine($"Minimum: {minScore}");
            report.WriteLine($"Maximum: {maxScore}");
        }
        else
        {
            report.WriteLine("No valid rows found.");
        }

        Console.WriteLine("Report generated: report.txt");
    }
}
