// This helper example focuses on isolating one scope-sensitive helper so lifetime differences stay visible.

// This extra example extends scope and lifetime basics with a session summary.

using System;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class Program
{
    const int BonusPoints = 5;
    const int PassingScore = 70;

    static (string Line, bool Passed) SummarizeAttempt(string name, int score)
    {
        int effectiveScore = score + BonusPoints;
        bool passed = effectiveScore >= PassingScore;
        string status = passed ? "passed" : "needs review";
        return ($"{name}: raw={score}, effective={effectiveScore}, status={status}", passed);
    }

    static void Main()
    {
        (string Name, int Score)[] attempts = { ("Ana", 64), ("Bruno", 71), ("Carla", 58) };
        int passedCount = 0;

        foreach (var attempt in attempts)
        {
            (string line, bool passed) = SummarizeAttempt(attempt.Name, attempt.Score);
            Console.WriteLine(line);
            if (passed)
            {
                passedCount++;
            }
        }

        Console.WriteLine($"Students above the target: {passedCount}");
    }
}
