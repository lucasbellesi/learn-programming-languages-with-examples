// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

// Helper setup for concurrency basics; this keeps the walkthrough readable.
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
    // Walk through one fixed scenario so concurrency basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key concurrency basics path.
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
        // Report values so learners can verify the concurrency basics outcome.
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
