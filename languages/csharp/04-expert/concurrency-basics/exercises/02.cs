using System;
using System.Collections.Generic;
using System.Threading;
using System.Threading.Tasks;

sealed class ProducerConsumerQueue
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
    static void Main()
    {
        Console.Write("Items to produce: ");
        if (!int.TryParse(Console.ReadLine(), out int count))
        {
            Console.WriteLine("Invalid item count.");
            return;
        }

        if (count < 0)
        {
            Console.WriteLine("Item count cannot be negative.");
            return;
        }

        ProducerConsumerQueue queue = new ProducerConsumerQueue();
        int consumed = 0;

        Task producer = Task.Run(() =>
        {
            for (int value = 1; value <= count; value++)
            {
                queue.Enqueue(value);
                Console.WriteLine($"Produced {value}");
                Thread.Sleep(5);
            }

            queue.Complete();
        });

        Task consumer = Task.Run(() =>
        {
            while (queue.TryDequeue(out int value))
            {
                consumed++;
                Console.WriteLine($"Consumed {value}");
            }
        });

        Task.WaitAll(producer, consumer);
        Console.WriteLine($"Produced total: {count}");
        Console.WriteLine($"Consumed total: {consumed}");
    }
}
