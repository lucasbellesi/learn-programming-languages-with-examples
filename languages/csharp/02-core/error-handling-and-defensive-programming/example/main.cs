// Module focus: Guarding risky inputs so failures stay explicit and controlled.
// Why it matters: the example makes it possible to separate expected failures from programming
// defects before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to separate expected failures from
// programming defects.
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

    // Fixed inputs make the consequence of continuing execution after detecting an invalid state
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        (double left, double right)[] scenarios = new[] { (42.0, 6.0), (10.0, 0.0) };

        foreach ((double left, double right) in scenarios)
        {
            // The printed result shows whether the program can preserve valid state and useful
            // diagnostics when operations fail.
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
