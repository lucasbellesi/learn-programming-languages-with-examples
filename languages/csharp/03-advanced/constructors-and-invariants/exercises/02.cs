using System;

class SimpleDate
{
    private readonly int month;
    private readonly int day;

    public SimpleDate(int monthValue, int dayValue)
    {
        month = monthValue;
        day = dayValue;
    }

    public bool IsValid()
    {
        if (month < 1 || month > 12)
        {
            return false;
        }

        int[] daysInMonth = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        return day >= 1 && day <= daysInMonth[month - 1];
    }
}

class Program
{
    static void Main()
    {
        Console.Write("Enter month and day: ");
        string raw = Console.ReadLine() ?? string.Empty;
        string[] parts = raw.Split(' ', StringSplitOptions.RemoveEmptyEntries);

        if (parts.Length != 2 ||
            !int.TryParse(parts[0], out int month) ||
            !int.TryParse(parts[1], out int day))
        {
            Console.WriteLine("Invalid input.");
            return;
        }

        SimpleDate date = new SimpleDate(month, day);
        Console.WriteLine(date.IsValid() ? "Valid date" : "Invalid date");
    }
}
