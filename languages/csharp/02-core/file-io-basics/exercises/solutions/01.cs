using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.Write("Input file path: ");
        string inputPath = (Console.ReadLine() ?? string.Empty).Trim();

        Console.Write("Output file path: ");
        string outputPath = (Console.ReadLine() ?? string.Empty).Trim();

        if (string.IsNullOrWhiteSpace(inputPath) || string.IsNullOrWhiteSpace(outputPath))
        {
            Console.WriteLine("Both paths are required.");
            return;
        }

        if (!File.Exists(inputPath))
        {
            Console.WriteLine("Could not open input file.");
            return;
        }

        try
        {
            int lineNumber = 1;
            using StreamReader reader = new StreamReader(inputPath);
            using StreamWriter writer = new StreamWriter(outputPath, false);

            string? line;
            while ((line = reader.ReadLine()) is not null)
            {
                writer.WriteLine($"{lineNumber}: {line}");
                lineNumber++;
            }

            Console.WriteLine($"Copied {lineNumber - 1} lines.");
        }
        catch (IOException)
        {
            Console.WriteLine("File processing failed.");
        }
    }
}
