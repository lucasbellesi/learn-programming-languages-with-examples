// This example shows starting multiple units of work and combining their results safely.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
sealed class WorkQueue
{
    private readonly Queue<int> items = new Queue<int>();
    private bool completed;

    public void Enqueue(int value)
    {
        lock (items)
        {
            items.Enqueue(value);
            Monitor.PulseAll(items);
        }
    }

    public bool TryDequeue(out int value)
    {
        lock (items)
        {
            while (items.Count == 0 && !completed)
            {
                Monitor.Wait(items);
            }

            if (items.Count == 0)
            {
                value = 0;
                return false;
            }

            value = items.Dequeue();
            return true;
        }
    }

    public void Complete()
    {
        lock (items)
        {
            completed = true;
            Monitor.PulseAll(items);
        }
    }
}

class Program
{
    // Run one deterministic scenario so the console output makes starting multiple units of work and combining their results safely easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        const int workerCount = 4;
        const int incrementsPerWorker = 10000;

        int counter = 0;
        object counterGate = new object();
        Task[] workers = new Task[workerCount];

        for (int workerIndex = 0; workerIndex < workerCount; workerIndex++)
        {
            workers[workerIndex] = Task.Run(() =>
            {
                for (int step = 0; step < incrementsPerWorker; step++)
                {
                    lock (counterGate)
                    {
                        counter++;
                    }
                }
            });
        }

        Task.WaitAll(workers);
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"Expected counter: {workerCount * incrementsPerWorker}");
        Console.WriteLine($"Actual counter: {counter}");

        Console.WriteLine("Producer-consumer demo:");

        WorkQueue queue = new WorkQueue();
        int consumedTotal = 0;
        object totalGate = new object();

        Task producer = Task.Run(() =>
        {
            foreach (int value in new[] { 10, 20, 30, 40 })
            {
                queue.Enqueue(value);
                Console.WriteLine($"Produced {value}");
                Thread.Sleep(10);
            }

            queue.Complete();
        });

        Task consumer = Task.Run(() =>
        {
            while (queue.TryDequeue(out int value))
            {
                lock (totalGate)
                {
                    consumedTotal += value;
                }

                Console.WriteLine($"Consumed {value}");
            }
        });

        Task.WaitAll(producer, consumer);
        Console.WriteLine($"Consumed total: {consumedTotal}");
    }
}
