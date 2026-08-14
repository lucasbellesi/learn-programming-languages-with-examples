using System;
using System.Collections.Generic;

interface IOperation
{
    bool TryApply(int left, int right, out int result);
}

sealed class AddOperation : IOperation
{
    public bool TryApply(int left, int right, out int result)
    {
        result = left + right;
        return true;
    }
}

sealed class MultiplyOperation : IOperation
{
    public bool TryApply(int left, int right, out int result)
    {
        result = left * right;
        return true;
    }
}

sealed class DivideOperation : IOperation
{
    public bool TryApply(int left, int right, out int result)
    {
        if (right == 0)
        {
            result = 0;
            return false;
        }

        result = left / right;
        return true;
    }
}

class Program
{
    static void Main()
    {
        Dictionary<string, IOperation> operations = new Dictionary<string, IOperation>(
            StringComparer.OrdinalIgnoreCase
        )
        {
            ["add"] = new AddOperation(),
            ["mul"] = new MultiplyOperation(),
            ["div"] = new DivideOperation(),
        };

        Console.Write("Command and two integers: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (
            parts.Length != 3
            || !int.TryParse(parts[1], out int left)
            || !int.TryParse(parts[2], out int right)
        )
        {
            Console.WriteLine("Invalid input.");
            return;
        }

        if (!operations.TryGetValue(parts[0], out IOperation? operation))
        {
            Console.WriteLine("Unsupported command.");
            return;
        }

        if (!operation.TryApply(left, right, out int result))
        {
            Console.WriteLine("Operation failed.");
            return;
        }

        Console.WriteLine($"Result: {result}");
    }
}
