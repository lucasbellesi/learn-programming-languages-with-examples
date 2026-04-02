// This helper example focuses on focusing on the retry loop so invalid input handling is easy to trace.

// This extra example extends types-and-io with a validation loop.

using System;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Program
{
    static void Main()
    {
        Console.Write("Enter your full name: ");
        string fullName = (Console.ReadLine() ?? string.Empty).Trim();

        int age;
        while (true)
        {
            Console.Write("Enter your age (1-120): ");
            if (!int.TryParse(Console.ReadLine(), out age))
            {
                Console.WriteLine("Invalid input. Please enter a number.");
                continue;
            }

            if (age < 1 || age > 120)
            {
                Console.WriteLine("Age must be between 1 and 120.");
                continue;
            }

            break;
        }

        Console.WriteLine("\nRegistration summary:");
        Console.WriteLine($"Name: {fullName}");
        Console.WriteLine($"Age: {age}");
    }
}
