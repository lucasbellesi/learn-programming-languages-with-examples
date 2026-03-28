// This extra example extends formatted output with a compact score report.
// Example purpose: align labels, numbers, and a final summary row.

using System;

class Program
{
    static void Main()
    {
        (string Name, int Score, int Tasks)[] rows =
        {
            ("Ana", 91, 4),
            ("Bruno", 77, 3),
            ("Carla", 88, 5),
        };

        Console.WriteLine($"{"Student", -10}{"Score", 8}{"Tasks", 8}{"Average", 10}");
        Console.WriteLine(new string('-', 36));

        int weightedTotal = 0;
        int taskTotal = 0;
        foreach (var row in rows)
        {
            double average = (double)row.Score / row.Tasks;
            weightedTotal += row.Score;
            taskTotal += row.Tasks;
            Console.WriteLine($"{row.Name, -10}{row.Score, 8}{row.Tasks, 8}{average, 10:F2}");
        }

        Console.WriteLine(new string('-', 36));
        Console.WriteLine(
            $"{"Totals", -10}{weightedTotal, 8}{taskTotal, 8}{(double)weightedTotal / taskTotal, 10:F2}"
        );
    }
}
