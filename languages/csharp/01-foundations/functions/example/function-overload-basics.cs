// This helper example focuses on showing one focused overload or helper so the main example stays easy to scan.

// This extra example extends functions with overload-style dispatch.

using System;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Program
{
    static void PrintValue(int value)
    {
        Console.WriteLine($"Integer value: {value}");
    }

    static void PrintValue(double value)
    {
        Console.WriteLine($"Double value: {value}");
    }

    static void PrintValue(string value)
    {
        Console.WriteLine($"String value: {value}");
    }

    static void Main()
    {
        PrintValue(42);
        PrintValue(3.14159);
        PrintValue("Hello from function overloads");
    }
}
