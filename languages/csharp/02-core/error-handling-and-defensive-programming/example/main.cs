// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static bool TrySafeDivide(double left, double right, out double result)
    {
        // Intent: block invalid operations early before the main logic continues.
        if (right == 0.0)
        {
            result = 0.0;
            return false;
        }

        result = left / right;
        return true;
    }

    static void Main()
    {
        // Program flow: run a fixed set of cases to show both safe and unsafe paths.
        (double left, double right)[] scenarios = new[]
        {
            (42.0, 6.0),
            (10.0, 0.0)
        };

        foreach ((double left, double right) in scenarios)
        {
            // Intent: print scenario input so behavior is easy to verify.
            Console.WriteLine($"Input: {left} {right}");

            if (!TrySafeDivide(left, right, out double quotient))
            {
                Console.WriteLine("Cannot divide by zero.");
                continue;
            }

            // Intent: print deterministic final output for quick verification.
            Console.WriteLine($"Result: {quotient}");
        }
    }
}
