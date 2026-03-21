using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many products? ");
        int count = int.Parse(Console.ReadLine() ?? "0");

        if (count <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        var products = new List<(string Name, double Price, int Quantity)>();

        for (int i = 0; i < count; i++)
        {
            Console.Write($"Product {i + 1} name: ");
            string name = Console.ReadLine() ?? "";

            Console.Write($"Product {i + 1} price: ");
            double price = double.Parse(Console.ReadLine() ?? "0");

            Console.Write($"Product {i + 1} quantity: ");
            int quantity = int.Parse(Console.ReadLine() ?? "0");

            products.Add((name, price, quantity));
        }

        Console.WriteLine($"{"Product",-16}{"Price",10}{"Qty",8}{"Total",12}");
        Console.WriteLine(new string('-', 46));

        double grandTotal = 0;
        foreach (var product in products)
        {
            double total = product.Price * product.Quantity;
            grandTotal += total;
            Console.WriteLine($"{product.Name,-16}{product.Price,10:F2}{product.Quantity,8}{total,12:F2}");
        }

        Console.WriteLine(new string('-', 46));
        Console.WriteLine($"{"Grand total",-34}{grandTotal,12:F2}");
    }
}
