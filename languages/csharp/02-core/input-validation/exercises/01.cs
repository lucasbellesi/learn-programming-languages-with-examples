using System;

class Program
{
    static int ReadIntInRange(string prompt, int minValue, int maxValue)
    {
        while (true)
        {
            Console.Write(prompt);
            string? raw = Console.ReadLine();
            if (!int.TryParse(raw, out int value))
            {
                Console.WriteLine("Invalid input. Please enter an integer.");
                continue;
            }

            if (value < minValue || value > maxValue)
            {
                Console.WriteLine("Out of range. Try again.");
                continue;
            }

            return value;
        }
    }

    static void Main()
    {
        int value = ReadIntInRange("Enter an integer from 1 to 100: ", 1, 100);
        Console.WriteLine($"Square: {value * value}");
    }
}
