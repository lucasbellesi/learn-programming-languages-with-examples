using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter total seconds: ");
        int totalSeconds = int.Parse(Console.ReadLine() ?? "0");

        if (totalSeconds < 0)
        {
            Console.WriteLine("Please enter a non-negative value.");
            return;
        }

        int hours = totalSeconds / 3600;
        int minutes = (totalSeconds % 3600) / 60;
        int seconds = totalSeconds % 60;

        Console.WriteLine($"Hours: {hours}");
        Console.WriteLine($"Minutes: {minutes}");
        Console.WriteLine($"Seconds: {seconds}");
    }
}
