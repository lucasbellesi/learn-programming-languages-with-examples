// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Threading.Tasks;

class Program
{
    // Walk through one fixed counter scenario so concurrency behavior stays repeatable.
    static void Main()
    {
        const int workerCount = 4;
        const int incrementsPerWorker = 10000;

        int counter = 0;
        object counterGate = new object();
        Task[] workers = new Task[workerCount];

        // Start several workers that all update the same value.
        for (int workerIndex = 0; workerIndex < workerCount; workerIndex++)
        {
            workers[workerIndex] = Task.Run(() =>
            {
                for (int step = 0; step < incrementsPerWorker; step++)
                {
                    // The lock keeps each increment from overlapping another worker's increment.
                    lock (counterGate)
                    {
                        counter++;
                    }
                }
            });
        }

        Task.WaitAll(workers);

        // Report values so learners can verify that protected shared state stayed consistent.
        Console.WriteLine($"Expected counter: {workerCount * incrementsPerWorker}");
        Console.WriteLine($"Actual counter: {counter}");
        Console.WriteLine($"Counter is correct: {counter == workerCount * incrementsPerWorker}");
    }
}
