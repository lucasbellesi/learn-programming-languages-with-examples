// This helper example focuses on focusing on how one operation changes later ownership or shared state.

// This extra example extends copy-and-move semantics with inventory transfer.

using System;
using System.Collections.Generic;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Inventory
{
    private List<string> items;

    public Inventory(IEnumerable<string> sourceItems)
    {
        items = new List<string>(sourceItems);
    }

    private Inventory(List<string> itemsValue)
    {
        items = itemsValue;
    }

    public Inventory Clone()
    {
        return new Inventory(new List<string>(items));
    }

    public Inventory Transfer()
    {
        List<string> movedItems = items;
        items = new List<string>();
        return new Inventory(movedItems);
    }

    public List<string> Items => items;
}

class Program
{
    static void Main()
    {
        Inventory original = new Inventory(new[] { "Notebook", "Pencil" });
        Inventory alias = original;
        Inventory clone = original.Clone();
        Inventory transferred = original.Transfer();

        alias.Items.Add("Marker");
        clone.Items.Add("Eraser");

        Console.WriteLine($"original items: [{string.Join(", ", original.Items)}]");
        Console.WriteLine($"alias items: [{string.Join(", ", alias.Items)}]");
        Console.WriteLine($"clone items: [{string.Join(", ", clone.Items)}]");
        Console.WriteLine($"transferred items: [{string.Join(", ", transferred.Items)}]");
    }
}
