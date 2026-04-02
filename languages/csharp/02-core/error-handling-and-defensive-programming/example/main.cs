// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: practicing error handling and defensive programming patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for error handling and defensive programming; this keeps the walkthrough readable.
class Program
{
    static bool TrySafeDivide(double left, double right, out double result)
    {
        if (right == 0.0)
        {
            result = 0.0;
            return false;
        }

        result = left / right;
        return true;
    }

    // Walk through one fixed scenario so error handling and defensive programming behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key error handling and defensive programming path.
        (double left, double right)[] scenarios = new[] { (42.0, 6.0), (10.0, 0.0) };

        foreach ((double left, double right) in scenarios)
        {
            // Report values so learners can verify the error handling and defensive programming outcome.
            Console.WriteLine($"Input: {left} {right}");

            if (!TrySafeDivide(left, right, out double quotient))
            {
                Console.WriteLine("Cannot divide by zero.");
                continue;
            }

            Console.WriteLine($"Result: {quotient}");
        }
    }
}
