// Module focus: How names stay visible only inside the blocks that own them.
// Why it matters: the example makes it possible to predict name visibility across nested scopes
// before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to predict name visibility across nested
// scopes.
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

    // Fixed inputs make the consequence of using values before they are assigned in all branches
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can explain when values and resources
        // cease to be usable.
        Console.Write("Enter score: ");
        int score = int.Parse(Console.ReadLine() ?? "0");

        string grade = Classify(score);
        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Passed: {score >= PassingScore}");
    }
}
