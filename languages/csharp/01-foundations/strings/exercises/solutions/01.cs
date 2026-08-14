using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter text: ");
        string line = Console.ReadLine() ?? "";

        string[] words = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        Console.WriteLine($"Word count: {words.Length}");
    }
}
