using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter product price quantity: ");
        string? line = Console.ReadLine();
        string[] parts = (line ?? "").Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (parts.Length != 3)
        {
            Console.WriteLine("Invalid format. Use: product price quantity");
            return;
        }

        string product = parts[0];
        double price = double.Parse(parts[1]);
        int quantity = int.Parse(parts[2]);

        double total = price * quantity;
        Console.WriteLine($"Product: {product}");
        Console.WriteLine($"Total price: {total:F2}");
    }
}
