// This extra example extends control-flow with a menu-driven loop.
// Example purpose: show repeated branching and state updates.

using System;

class Program
{
    static void Main()
    {
        int currentSum = 0;

        while (true)
        {
            Console.WriteLine("\nMenu");
            Console.WriteLine("1) Add number to sum");
            Console.WriteLine("2) Show current sum");
            Console.WriteLine("3) Reset sum");
            Console.WriteLine("4) Exit");
            Console.Write("Choose an option: ");

            string? choice = Console.ReadLine();
            switch (choice)
            {
                case "1":
                    Console.Write("Enter a number: ");
                    if (!int.TryParse(Console.ReadLine(), out int number))
                    {
                        Console.WriteLine("Invalid number. Try again.");
                        continue;
                    }

                    currentSum += number;
                    Console.WriteLine($"Added. New sum is {currentSum}.");
                    break;
                case "2":
                    Console.WriteLine($"Current sum: {currentSum}");
                    break;
                case "3":
                    currentSum = 0;
                    Console.WriteLine("Sum reset to 0.");
                    break;
                case "4":
                    Console.WriteLine("Goodbye.");
                    return;
                default:
                    Console.WriteLine("Invalid option. Try again.");
                    break;
            }
        }
    }
}
