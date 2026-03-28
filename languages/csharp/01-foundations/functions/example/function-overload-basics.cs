// This extra example extends functions with overload-style dispatch.
// Example purpose: show one method name handling multiple value types.

using System;

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
