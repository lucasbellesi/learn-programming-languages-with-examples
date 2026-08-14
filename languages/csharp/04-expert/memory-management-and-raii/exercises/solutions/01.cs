using System;

sealed class OwnedBuffer : IDisposable
{
    private int[]? values;
    private bool disposed;

    public OwnedBuffer(int length)
    {
        values = new int[length];
    }

    public int Length => values?.Length ?? 0;

    public void SetAt(int index, int value)
    {
        EnsureNotDisposed();
        values![index] = value;
    }

    public int GetAt(int index)
    {
        EnsureNotDisposed();
        return values![index];
    }

    public int Sum()
    {
        EnsureNotDisposed();

        int total = 0;
        foreach (int value in values!)
        {
            total += value;
        }

        return total;
    }

    public void Dispose()
    {
        if (disposed)
        {
            return;
        }

        disposed = true;
        values = null;
        GC.SuppressFinalize(this);
    }

    private void EnsureNotDisposed()
    {
        if (disposed)
        {
            throw new ObjectDisposedException(nameof(OwnedBuffer));
        }
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Count: ");
        if (!int.TryParse(Console.ReadLine(), out int count))
        {
            Console.WriteLine("Invalid count.");
            return;
        }

        if (count <= 0)
        {
            Console.WriteLine("Count must be positive.");
            return;
        }

        using OwnedBuffer buffer = new OwnedBuffer(count);

        for (int index = 0; index < buffer.Length; index++)
        {
            Console.Write($"Value {index + 1}: ");
            if (!int.TryParse(Console.ReadLine(), out int value))
            {
                Console.WriteLine("Invalid integer input.");
                return;
            }

            buffer.SetAt(index, value);
        }

        Console.WriteLine($"Sum: {buffer.Sum()}");
        Console.Write("Reversed: ");
        for (int index = buffer.Length - 1; index >= 0; index--)
        {
            Console.Write(buffer.GetAt(index));
            if (index > 0)
            {
                Console.Write(' ');
            }
        }

        Console.WriteLine();
    }
}
