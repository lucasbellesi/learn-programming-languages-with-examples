using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter row (name,age,city): ");
        string row = Console.ReadLine() ?? string.Empty;

        int firstComma = row.IndexOf(',');
        if (firstComma < 0)
        {
            Console.WriteLine("Invalid format. Missing commas.");
            return;
        }

        int secondComma = row.IndexOf(',', firstComma + 1);
        if (secondComma < 0)
        {
            Console.WriteLine("Invalid format. Missing second comma.");
            return;
        }

        string name = row.Substring(0, firstComma);
        string age = row.Substring(firstComma + 1, secondComma - firstComma - 1);
        string city = row.Substring(secondComma + 1);

        if (name.Length == 0 || age.Length == 0 || city.Length == 0)
        {
            Console.WriteLine("Invalid format. Empty field detected.");
            return;
        }

        Console.WriteLine($"Name: {name}");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"City: {city}");
    }
}
