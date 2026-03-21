using System;
using System.Collections.Generic;

class IntBuffer
{
    private List<int> values;

    public IntBuffer(int size)
    {
        int safeSize = size < 0 ? 0 : size;
        values = new List<int>(new int[safeSize]);
        Console.WriteLine($"Constructed IntBuffer (size={values.Count})");
    }

    private IntBuffer(List<int> sourceValues)
    {
        values = sourceValues;
        Console.WriteLine($"Transferred IntBuffer (size={values.Count})");
    }

    public IntBuffer Clone()
    {
        IntBuffer copy = new IntBuffer(0);
        copy.values = new List<int>(values);
        Console.WriteLine("Cloned IntBuffer");
        return copy;
    }

    public IntBuffer Transfer()
    {
        List<int> movedValues = values;
        values = new List<int>();
        return new IntBuffer(movedValues);
    }

    public int Size => values.Count;
}

class Program
{
    static void Main()
    {
        IntBuffer a = new IntBuffer(4);
        IntBuffer b = a.Clone();
        IntBuffer c = b.Transfer();

        Console.WriteLine($"a size: {a.Size}");
        Console.WriteLine($"b size: {b.Size}");
        Console.WriteLine($"c size: {c.Size}");
    }
}
