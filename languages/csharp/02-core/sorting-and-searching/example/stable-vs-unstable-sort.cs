// This helper example focuses on contrasting two sorting behaviors without extra setup noise.

// This extra example extends sorting-and-searching with tie-order comparisons.

using System;
using System.Collections.Generic;
using System.Linq;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Record
{
    public int Score { get; init; }

    public string Name { get; init; } = string.Empty;
}

class Program
{
    static void PrintRecords(IEnumerable<Record> records, string title)
    {
        Console.WriteLine(title);
        foreach (Record record in records)
        {
            Console.WriteLine($"- score={record.Score}, name={record.Name}");
        }
        Console.WriteLine();
    }

    static void Main()
    {
        List<Record> records = new List<Record>
        {
            new Record { Score = 90, Name = "Ana" },
            new Record { Score = 75, Name = "Bob" },
            new Record { Score = 90, Name = "Carla" },
            new Record { Score = 75, Name = "Diego" },
            new Record { Score = 90, Name = "Emma" },
        };

        PrintRecords(records, "Original order:");

        List<Record> unstable = new List<Record>(records);
        unstable.Sort((left, right) => left.Score.CompareTo(right.Score));
        PrintRecords(unstable, "After List.Sort (not guaranteed stable):");

        List<Record> stable = records.OrderBy(record => record.Score).ToList();
        PrintRecords(stable, "After LINQ OrderBy (stable):");

        Console.WriteLine("Notice how equal scores keep relative order with OrderBy.");
    }
}
