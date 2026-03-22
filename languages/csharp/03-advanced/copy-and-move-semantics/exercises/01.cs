using System;
using System.Collections.Generic;

class IntBuffer
{
    private List<int> values;

    public IntBuffer(List<int> initialValues)
    {
        values = new List<int>(initialValues);
        Console.WriteLine($"Constructed IntBuffer (size={values.Count})");
    }

    private IntBuffer(List<int> sourceValues)
    {
        values = sourceValues;
    }

    public IntBuffer Clone()
    {
        IntBuffer copy = new IntBuffer(new List<int>(values));
        Console.WriteLine("Cloned IntBuffer");
        return copy;
    }

    public IntBuffer Transfer()
    {
        List<int> movedValues = values;
        values = new List<int>();
        IntBuffer transferred = new IntBuffer(movedValues);
        Console.WriteLine($"Transferred IntBuffer (size={transferred.Size})");
        return transferred;
    }

    public int Size => values.Count;
}

class Program
{
    static void Main()
    {
        Console.Write("Buffer size: ");
        if (!int.TryParse(Console.ReadLine(), out int size) || size < 0)
        {
            Console.WriteLine("Invalid size.");
            return;
        }

        Console.Write("Buffer values: ");
        string rawValues = Console.ReadLine() ?? string.Empty;
        string[] parts = rawValues.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        if (parts.Length != size)
        {
            Console.WriteLine("The amount of values must match the buffer size.");
            return;
        }

        List<int> parsedValues = new List<int>(size);
        foreach (string part in parts)
        {
            if (!int.TryParse(part, out int parsed))
            {
                Console.WriteLine("Invalid value detected.");
                return;
            }

            parsedValues.Add(parsed);
        }

        IntBuffer a = new IntBuffer(parsedValues);
        IntBuffer b = a.Clone();
        IntBuffer c = b.Transfer();

        Console.WriteLine($"a size: {a.Size}");
        Console.WriteLine($"b size: {b.Size}");
        Console.WriteLine($"c size: {c.Size}");
    }
}
