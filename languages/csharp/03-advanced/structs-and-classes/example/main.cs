// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to reason about.

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

// Helper setup for structs and classes; this keeps the walkthrough readable.
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
    // Walk through one fixed scenario so structs and classes behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key structs and classes path.
        List<Coordinate> route = new List<Coordinate>
        {
            new Coordinate(2, 3),
            new Coordinate(-1, 4),
            new Coordinate(5, -2),
        };

        // Report values so learners can verify the structs and classes outcome.
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
