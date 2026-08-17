using System;

sealed class Document
{
    public Document(string name)
    {
        Name = name;
    }

    public string Name { get; }
}

sealed class DocumentSlot
{
    public DocumentSlot(string label, Document? current)
    {
        Label = label;
        Current = current;
    }

    public string Label { get; }

    public Document? Current { get; private set; }

    public void MoveTo(DocumentSlot destination)
    {
        if (Current is null)
        {
            Console.WriteLine($"{Label} is empty.");
            return;
        }
        if (destination.Current is not null)
        {
            Console.WriteLine($"{destination.Label} is occupied.");
            return;
        }

        Console.WriteLine($"{Label} moves {Current.Name} to {destination.Label}.");
        destination.Current = Current;
        Current = null;
    }

    public void Print()
    {
        Console.WriteLine($"{Label}: {(Current is null ? "empty" : Current.Name)}");
    }
}

class Program
{
    static void Main()
    {
        string sourceName = Console.ReadLine() ?? "empty";
        string destinationName = Console.ReadLine() ?? "empty";
        DocumentSlot active = new DocumentSlot(
            "Source",
            sourceName == "empty" ? null : new Document(sourceName)
        );
        DocumentSlot backup = new DocumentSlot(
            "Destination",
            destinationName == "empty" ? null : new Document(destinationName)
        );

        active.Print();
        backup.Print();
        active.MoveTo(backup);
        active.Print();
        backup.Print();
    }
}
