using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;

class Program
{
    static int BucketForScore(int score)
    {
        return score == 100 ? 9 : score / 10;
    }

    static void WriteLineBoth(StreamWriter writer, string line)
    {
        Console.WriteLine(line);
        writer.WriteLine(line);
    }

    static void Main()
    {
        using StreamWriter report = new StreamWriter("core_assessment_report.txt");

        List<int> values = new List<int>();
        int[] buckets = new int[10];

        Console.WriteLine("Enter integer values (0-100). End with -1.");
        bool stopReading = false;
        while (true)
        {
            string raw = Console.ReadLine() ?? string.Empty;
            string[] tokens = raw.Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries);
            if (tokens.Length == 0)
            {
                continue;
            }

            foreach (string token in tokens)
            {
                if (!int.TryParse(token, out int value))
                {
                    Console.WriteLine($"Ignoring invalid token: {token}");
                    continue;
                }

                if (value == -1)
                {
                    stopReading = true;
                    break;
                }

                if (value < 0 || value > 100)
                {
                    Console.WriteLine($"Ignoring out-of-range value: {value}");
                    continue;
                }

                values.Add(value);
                buckets[BucketForScore(value)]++;
            }

            if (stopReading)
            {
                break;
            }
        }

        if (values.Count == 0)
        {
            WriteLineBoth(report, "No valid values were entered.");
            WriteLineBoth(report, "Report saved to core_assessment_report.txt");
            return;
        }

        int minValue = values[0];
        int maxValue = values[0];
        int sum = 0;
        foreach (int value in values)
        {
            sum += value;
            if (value < minValue)
            {
                minValue = value;
            }
            if (value > maxValue)
            {
                maxValue = value;
            }
        }

        double average = (double)sum / values.Count;
        WriteLineBoth(report, $"Valid count: {values.Count}");
        WriteLineBoth(report, $"Minimum: {minValue}");
        WriteLineBoth(report, $"Maximum: {maxValue}");
        WriteLineBoth(report, $"Average: {average.ToString(CultureInfo.InvariantCulture)}");
        WriteLineBoth(report, "Frequency table:");

        for (int index = 0; index < 10; index++)
        {
            int start = index * 10;
            int end = index == 9 ? 100 : start + 9;
            WriteLineBoth(report, $"{start}-{end}: {buckets[index]}");
        }

        WriteLineBoth(report, "Report saved to core_assessment_report.txt");
    }
}
