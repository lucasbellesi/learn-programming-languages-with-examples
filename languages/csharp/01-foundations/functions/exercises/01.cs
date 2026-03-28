using System;

class Program
{
    static int MaxOfThree(int a, int b, int c)
    {
        int maxValue = a;
        if (b > maxValue)
            maxValue = b;
        if (c > maxValue)
            maxValue = c;
        return maxValue;
    }

    static void Main()
    {
        Console.Write("Enter three integers: ");
        string[] parts = (Console.ReadLine() ?? "").Split(
            ' ',
            StringSplitOptions.RemoveEmptyEntries
        );

        if (parts.Length != 3)
        {
            Console.WriteLine("Please enter exactly three integers.");
            return;
        }

        int x = int.Parse(parts[0]);
        int y = int.Parse(parts[1]);
        int z = int.Parse(parts[2]);

        Console.WriteLine($"Maximum: {MaxOfThree(x, y, z)}");
    }
}
