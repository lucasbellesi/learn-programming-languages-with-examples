using System;

class Program
{
    const int PassingScore = 60;

    static string Classify(int score)
    {
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        if (score >= PassingScore) return "D";
        return "F";
    }

    static void Main()
    {
        Console.Write("Enter score: ");
        int score = int.Parse(Console.ReadLine() ?? "0");

        string grade = Classify(score);
        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Passed: {score >= PassingScore}");
    }
}
