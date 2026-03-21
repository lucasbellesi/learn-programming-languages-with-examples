// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    const int PassingScore = 60;

    static string Classify(int score)
    {
        // Intent: guard invalid or edge-case paths before the main path continues.
        if (score >= 90) return "A";
        if (score >= 80) return "B";
        if (score >= 70) return "C";
        if (score >= PassingScore) return "D";
        return "F";
    }

    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        // Intent: print intermediate or final output for quick behavior verification.
        Console.Write("Enter score: ");
        // Intent: gather typed input first so later operations are predictable.
        int score = int.Parse(Console.ReadLine() ?? "0");

        string grade = Classify(score);
        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Passed: {score >= PassingScore}");
    }
}
