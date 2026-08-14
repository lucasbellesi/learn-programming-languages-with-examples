using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter score (0-100): ");
        int score = int.Parse(Console.ReadLine() ?? "0");

        if (score < 0 || score > 100)
        {
            Console.WriteLine("Score must be between 0 and 100.");
            return;
        }

        string grade = "F";
        if (score >= 90)
        {
            grade = "A";
        }
        else if (score >= 80)
        {
            grade = "B";
        }
        else if (score >= 70)
        {
            grade = "C";
        }
        else if (score >= 60)
        {
            grade = "D";
        }

        Console.WriteLine($"Grade: {grade}");
    }
}
