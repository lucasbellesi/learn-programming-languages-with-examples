using System;
using System.Diagnostics;
using System.Text;

class Program
{
    static void Main()
    {
        Console.Write("Line count: ");
        if (!int.TryParse(Console.ReadLine(), out int lineCount))
        {
            Console.WriteLine("Invalid line count.");
            return;
        }

        if (lineCount < 0)
        {
            Console.WriteLine("Line count cannot be negative.");
            return;
        }

        long concatTicks = Measure(() => BuildWithConcatenation(lineCount));
        long builderTicks = Measure(() => BuildWithBuilder(lineCount));

        Console.WriteLine($"Concatenation ticks: {concatTicks}");
        Console.WriteLine($"StringBuilder ticks: {builderTicks}");
    }

    static long Measure(Action action)
    {
        Stopwatch stopwatch = Stopwatch.StartNew();
        action();
        stopwatch.Stop();
        return stopwatch.ElapsedTicks;
    }

    static string BuildWithConcatenation(int lineCount)
    {
        string text = string.Empty;
        for (int index = 0; index < lineCount; index++)
        {
            text += $"item-{index};";
        }

        return text;
    }

    static string BuildWithBuilder(int lineCount)
    {
        StringBuilder builder = new StringBuilder(lineCount * 8);
        for (int index = 0; index < lineCount; index++)
        {
            builder.Append("item-");
            builder.Append(index);
            builder.Append(';');
        }

        return builder.ToString();
    }
}
