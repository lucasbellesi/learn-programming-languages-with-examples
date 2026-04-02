// This example shows modeling related data and behavior with structured types.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;
using System.Collections.Generic;

readonly struct Coordinate
{
    public Coordinate(int x, int y)
    {
        X = x;
        Y = y;
    }

    public int X { get; }
    public int Y { get; }

    public int ManhattanDistanceFromOrigin()
    {
        return Math.Abs(X) + Math.Abs(Y);
    }

    public override string ToString()
    {
        return $"({X}, {Y})";
    }
}

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Wallet
{
    private readonly string owner;
    private decimal balance;

    public Wallet(string ownerName, decimal initialBalance)
    {
        owner = string.IsNullOrWhiteSpace(ownerName) ? "Unknown" : ownerName.Trim();

        balance = initialBalance < 0m ? 0m : initialBalance;
    }

    public bool Deposit(decimal amount)
    {
        if (amount <= 0m)
        {
            return false;
        }

        balance += amount;
        return true;
    }

    public bool Withdraw(decimal amount)
    {
        if (amount <= 0m || amount > balance)
        {
            return false;
        }

        balance -= amount;
        return true;
    }

    public string Owner => owner;
    public decimal Balance => balance;
}

class Program
{
    // Run one deterministic scenario so the console output makes modeling related data and behavior with structured types easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        List<Coordinate> route = new List<Coordinate>
        {
            new Coordinate(2, 3),
            new Coordinate(-1, 4),
            new Coordinate(5, -2),
        };

        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine("Coordinates (struct example):");
        foreach (Coordinate point in route)
        {
            Console.WriteLine(
                $"Point {point}, Manhattan distance = {point.ManhattanDistanceFromOrigin()}"
            );
        }

        Wallet wallet = new Wallet("Maya", 120m);
        wallet.Deposit(35m);
        wallet.Withdraw(40m);

        Console.WriteLine("\nWallet (class example):");
        Console.WriteLine($"Owner: {wallet.Owner}");
        Console.WriteLine($"Balance: {wallet.Balance}");
    }
}
