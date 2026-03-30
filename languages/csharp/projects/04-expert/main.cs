using System;
using System.Collections.Generic;
using System.Diagnostics;

sealed class Step
{
    private readonly string name;
    private int processedCount;

    public Step(string nameValue)
    {
        name = nameValue;
        processedCount = 0;
    }

    public string Name => name;

    public int ProcessedCount => processedCount;

    public void Run()
    {
        processedCount++;
    }
}

class Program
{
    static void Main()
    {
        const int jobCount = 3;

        List<Step> steps = new List<Step> { new Step("load"), new Step("transform") };

        Stopwatch stopwatch = Stopwatch.StartNew();

        for (int job = 0; job < jobCount; job++)
        {
            foreach (Step step in steps)
            {
                step.Run();
            }
        }

        stopwatch.Stop();
        long elapsedMicroseconds = (long)(stopwatch.Elapsed.TotalMilliseconds * 1000.0);

        Console.WriteLine($"Running {jobCount} jobs through {steps.Count} steps...");
        foreach (Step step in steps)
        {
            Console.WriteLine($"Step {step.Name} processed {step.ProcessedCount} jobs");
        }

        Console.WriteLine($"Elapsed (microseconds): {elapsedMicroseconds}");
    }
}
