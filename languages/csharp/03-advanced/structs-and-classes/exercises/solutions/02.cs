using System;

class Counter
{
    private int value;

    public void Increment()
    {
        value++;
    }

    public void Decrement()
    {
        value--;
    }

    public void Reset()
    {
        value = 0;
    }

    public int Value => value;
}

class Program
{
    static void Main()
    {
        Counter counter = new Counter();
        Console.WriteLine("Commands: inc, dec, reset, stop");

        while (true)
        {
            Console.Write("Enter command: ");
            string command = (Console.ReadLine() ?? string.Empty).Trim().ToLowerInvariant();

            if (command == "inc")
            {
                counter.Increment();
                Console.WriteLine($"Current value: {counter.Value}");
                continue;
            }

            if (command == "dec")
            {
                counter.Decrement();
                Console.WriteLine($"Current value: {counter.Value}");
                continue;
            }

            if (command == "reset")
            {
                counter.Reset();
                Console.WriteLine($"Current value: {counter.Value}");
                continue;
            }

            if (command == "stop")
            {
                break;
            }

            Console.WriteLine("Unknown command.");
        }

        Console.WriteLine($"Final value: {counter.Value}");
    }
}
