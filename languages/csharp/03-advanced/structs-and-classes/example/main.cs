// Module focus: Modeling related data and behavior with structured types.
// Why it matters: the example makes it possible to model data and behavior with cohesive domain
// types before the learner tackles the exercises.

using System;
using System.Collections.Generic;

class Program
{
    // Fixed inputs make the consequence of using mutable structs for shared state visible and
    // repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        List<Coordinate> route = new List<Coordinate>
        {
            new Coordinate(2, 3),
            new Coordinate(-1, 4),
            new Coordinate(5, -2),
        };

        // The printed result shows whether the program can protect invariants through
        // constructors and methods.
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
