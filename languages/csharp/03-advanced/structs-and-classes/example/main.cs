// Module focus: Modeling related data and behavior with structured types.
// Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to reason about.

using System;
using System.Collections.Generic;

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
