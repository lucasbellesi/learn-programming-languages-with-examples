// This example shows guarding risky inputs so failures stay explicit and controlled.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
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

    // Run one deterministic scenario so the console output makes guarding risky inputs so failures stay explicit and controlled easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        (double left, double right)[] scenarios = new[] { (42.0, 6.0), (10.0, 0.0) };

        foreach ((double left, double right) in scenarios)
        {
            // Print the observed state here so learners can connect the code path to a concrete result.
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
