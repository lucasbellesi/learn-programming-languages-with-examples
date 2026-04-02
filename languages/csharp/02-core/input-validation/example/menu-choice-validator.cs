// This helper example focuses on isolating the guard logic that accepts only valid menu choices.

// This extra example extends input validation with a menu choice validator.

using System;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Program
{
    static string ReadMenuChoice()
    {
        while (true)
        {
            Console.Write("Choose [1] Add, [2] Remove, [3] Exit: ");
            string choice = (Console.ReadLine() ?? string.Empty).Trim();
            if (choice == "1" || choice == "2" || choice == "3")
            {
                return choice;
            }

            Console.WriteLine("Option must be 1, 2, or 3.");
        }
    }

    static int ReadQuantity()
    {
        while (true)
        {
            Console.Write("Enter quantity (1-9): ");
            if (!int.TryParse(Console.ReadLine(), out int quantity))
            {
                Console.WriteLine("Quantity must be an integer.");
                continue;
            }

            if (quantity >= 1 && quantity <= 9)
            {
                return quantity;
            }

            Console.WriteLine("Quantity must be between 1 and 9.");
        }
    }

    static void Main()
    {
        string choice = ReadMenuChoice();
        if (choice == "3")
        {
            Console.WriteLine("Nothing to process.");
            return;
        }

        int quantity = ReadQuantity();
        string action = choice == "1" ? "added" : "removed";
        Console.WriteLine($"{quantity} item(s) {action}.");
    }
}
