using System;

class Program
{
    static void Main()
    {
        Console.Write("How many numbers? ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        if (n <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        Console.Write("Value 1: ");
        double first = double.Parse(Console.ReadLine() ?? "0");
        double sum = first;
        double min = first;
        double max = first;

        for (int i = 2; i <= n; i++)
        {
            Console.Write($"Value {i}: ");
            double value = double.Parse(Console.ReadLine() ?? "0");
            sum += value;
            if (value < min)
                min = value;
            if (value > max)
                max = value;
        }

        Console.WriteLine($"Sum: {sum:F4}");
        Console.WriteLine($"Average: {sum / n:F4}");
        Console.WriteLine($"Minimum: {min:F4}");
        Console.WriteLine($"Maximum: {max:F4}");
    }
}
