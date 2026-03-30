using System;
using System.Collections.Generic;
using System.Threading.Tasks;

sealed class DataSet
{
    public DataSet(List<int> values)
    {
        Values = values;
    }

    public List<int> Values { get; }
}

sealed class Summary
{
    public long Total { get; set; }
    public int Minimum { get; set; } = int.MaxValue;
    public int Maximum { get; set; } = int.MinValue;
}

class Program
{
    static void Main()
    {
        DataSet data = new DataSet(new List<int> { 12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6 });

        int workerCount = 3;
        int chunkSize = (data.Values.Count + workerCount - 1) / workerCount;
        Summary globalSummary = new Summary();
        object gate = new object();

        Task[] tasks = new Task[workerCount];

        for (int workerId = 0; workerId < workerCount; workerId++)
        {
            int capturedWorkerId = workerId;
            int begin = capturedWorkerId * chunkSize;
            int end = Math.Min(begin + chunkSize, data.Values.Count);

            tasks[capturedWorkerId] = Task.Run(() =>
            {
                if (begin >= end)
                {
                    return;
                }

                long localTotal = 0;
                int localMin = data.Values[begin];
                int localMax = data.Values[begin];

                for (int index = begin; index < end; index++)
                {
                    int value = data.Values[index];
                    localTotal += value;

                    if (value < localMin)
                    {
                        localMin = value;
                    }

                    if (value > localMax)
                    {
                        localMax = value;
                    }
                }

                lock (gate)
                {
                    Console.WriteLine($"Worker {capturedWorkerId} partial sum: {localTotal}");
                    globalSummary.Total += localTotal;
                    if (localMin < globalSummary.Minimum)
                    {
                        globalSummary.Minimum = localMin;
                    }

                    if (localMax > globalSummary.Maximum)
                    {
                        globalSummary.Maximum = localMax;
                    }
                }
            });
        }

        Task.WaitAll(tasks);

        Console.WriteLine();
        Console.WriteLine("Final summary:");
        Console.WriteLine($"Total: {globalSummary.Total}");
        Console.WriteLine($"Minimum: {globalSummary.Minimum}");
        Console.WriteLine($"Maximum: {globalSummary.Maximum}");
    }
}
