using System;
using System.IO;

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

    static void Main()
    {
        Console.Write("Enter file path (name score rows): ");
        string path = (Console.ReadLine() ?? string.Empty).Trim();

        if (!File.Exists(path))
        {
            Console.WriteLine("Could not open file.");
            return;
        }

        int validRows = 0;
        int invalidRows = 0;
        int sum = 0;

        try
        {
            using StreamReader reader = new StreamReader(path);
            string? line;
            while ((line = reader.ReadLine()) is not null)
            {
                if (TryParseScoreRow(line, out _, out int score))
                {
                    validRows++;
                    sum += score;
                }
                else
                {
                    invalidRows++;
                }
            }
        }
        catch (IOException)
        {
            Console.WriteLine("File processing failed.");
            return;
        }

        Console.WriteLine($"Valid rows: {validRows}");
        Console.WriteLine($"Invalid rows: {invalidRows}");

        if (validRows > 0)
        {
            double average = (double)sum / validRows;
            Console.WriteLine($"Average score: {average:F2}");
        }
        else
        {
            Console.WriteLine("No valid rows found.");
        }
    }
}
