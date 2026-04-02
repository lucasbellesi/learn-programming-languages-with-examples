// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: practicing scope and lifetime basics patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for scope and lifetime basics; this keeps the walkthrough readable.
class Program
{
    const int PassingScore = 60;

    static string Classify(int score)
    {
        if (score >= 90)
            return "A";
        if (score >= 80)
            return "B";
        if (score >= 70)
            return "C";
        if (score >= PassingScore)
            return "D";
        return "F";
    }

    // Walk through one fixed scenario so scope and lifetime basics behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key scope and lifetime basics path.
        // Report values so learners can verify the scope and lifetime basics outcome.
        Console.Write("Enter score: ");
        int score = int.Parse(Console.ReadLine() ?? "0");

        string grade = Classify(score);
        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Passed: {score >= PassingScore}");
    }
}
