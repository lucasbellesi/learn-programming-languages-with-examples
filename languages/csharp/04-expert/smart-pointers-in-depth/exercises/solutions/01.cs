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
        DocumentSlot active = new DocumentSlot("Active", new Document("Roadmap"));
        DocumentSlot backup = new DocumentSlot("Backup", new Document("Old Notes"));
        DocumentSlot empty = new DocumentSlot("Empty", null);

        active.Print();
        backup.Print();
        active.MoveTo(backup);
        active.Print();
        backup.Print();
        empty.MoveTo(active);
        empty.Print();
        active.Print();
    }
}
