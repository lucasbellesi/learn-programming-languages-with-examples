// Example purpose: show the module flow with clear, beginner-friendly steps.

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

class Wallet
{
    private readonly string owner;
    private decimal balance;

    public Wallet(string ownerName, decimal initialBalance)
    {
        owner = string.IsNullOrWhiteSpace(ownerName) ? "Unknown" : ownerName.Trim();

        // Intent: normalize invalid starting values to preserve class invariants.
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
    static void Main()
    {
        // Program flow: inspect value-type objects, then apply class-based state changes.
        List<Coordinate> route = new List<Coordinate>
        {
            new Coordinate(2, 3),
            new Coordinate(-1, 4),
            new Coordinate(5, -2),
        };

        Console.WriteLine("Coordinates (struct example):");
        // Intent: deterministic iteration helps beginners verify output quickly.
        foreach (Coordinate point in route)
        {
            Console.WriteLine(
                $"Point {point}, Manhattan distance = {point.ManhattanDistanceFromOrigin()}"
            );
        }

        Wallet wallet = new Wallet("Maya", 120m);
        wallet.Deposit(35m);
        wallet.Withdraw(40m);

        // Intent: report final state after guarded operations.
        Console.WriteLine("\nWallet (class example):");
        Console.WriteLine($"Owner: {wallet.Owner}");
        Console.WriteLine($"Balance: {wallet.Balance}");
    }
}
