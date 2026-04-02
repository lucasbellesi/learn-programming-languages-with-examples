// This example shows how names stay visible only inside the blocks that own them.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

    // Run one deterministic scenario so the console output makes how names stay visible only inside the blocks that own them easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.Write("Enter score: ");
        int score = int.Parse(Console.ReadLine() ?? "0");

        string grade = Classify(score);
        Console.WriteLine($"Grade: {grade}");
        Console.WriteLine($"Passed: {score >= PassingScore}");
    }
}
