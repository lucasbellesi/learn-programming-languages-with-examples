using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static void Main()
    {
        Console.Write("Values: ");
        string? numbersLine = Console.ReadLine();
        List<int> values = ParseValues(numbersLine);
        if (values.Count == 0)
        {
            Console.WriteLine("No values provided.");
            return;
        }

        Console.Write("Worker count: ");
        if (!int.TryParse(Console.ReadLine(), out int requestedWorkers))
        {
            Console.WriteLine("Invalid worker count.");
            return;
        }

        if (requestedWorkers <= 0)
        {
            Console.WriteLine("Worker count must be positive.");
            return;
        }

        int workerCount = Math.Min(requestedWorkers, values.Count);
        int chunkSize = (values.Count + workerCount - 1) / workerCount;
        Task<int>[] workers = new Task<int>[workerCount];

        for (int workerIndex = 0; workerIndex < workerCount; workerIndex++)
        {
            int start = workerIndex * chunkSize;
            int end = Math.Min(start + chunkSize, values.Count);
            int capturedIndex = workerIndex;

            workers[capturedIndex] = Task.Run(() =>
            {
                int partial = 0;
                for (int index = start; index < end; index++)
                {
                    partial += values[index];
                }

                return partial;
            });
        }

        Task.WaitAll(workers);

        int total = 0;
        for (int workerIndex = 0; workerIndex < workers.Length; workerIndex++)
        {
            int partial = workers[workerIndex].Result;
            total += partial;
            Console.WriteLine($"Worker {workerIndex + 1} partial: {partial}");
        }

        Console.WriteLine($"Total: {total}");
    }

    static List<int> ParseValues(string? raw)
    {
        List<int> values = new List<int>();
        if (string.IsNullOrWhiteSpace(raw))
        {
            return values;
        }

        string[] pieces = raw.Split(new[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
        foreach (string piece in pieces)
        {
            if (!int.TryParse(piece, out int value))
            {
                return new List<int>();
            }

            values.Add(value);
        }

        return values;
    }
}
