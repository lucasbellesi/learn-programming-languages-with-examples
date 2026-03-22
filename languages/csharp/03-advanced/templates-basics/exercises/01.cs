using System;

static class Helpers
{
    public static void SwapValues<T>(ref T left, ref T right)
    {
        T temp = left;
        left = right;
        right = temp;
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter two integers: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (parts.Length != 2 ||
            !int.TryParse(parts[0], out int left) ||
            !int.TryParse(parts[1], out int right))
        {
            Console.WriteLine("Invalid input.");
            return;
        }

        Console.WriteLine($"Before swap: {left} {right}");
        Helpers.SwapValues(ref left, ref right);
        Console.WriteLine($"After swap: {left} {right}");
    }
}
