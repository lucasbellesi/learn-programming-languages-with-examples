// This example shows building objects that start valid and stay valid through guarded updates.
// In C#, the example uses the standard library and static types to keep the workflow structured.

using System;

// Define the reusable pieces first so the main flow can focus on one observable scenario.
class Temperature
{
    private double celsius;

    public Temperature(double celsiusValue)
    {
        celsius = celsiusValue < -273.15 ? -273.15 : celsiusValue;
    }

    public bool SetCelsius(double newValue)
    {
        if (newValue < -273.15)
        {
            return false;
        }

        celsius = newValue;
        return true;
    }

    public double Celsius => celsius;
}

class Program
{
    // Run one deterministic scenario so the console output makes building objects that start valid and stay valid through guarded updates easy to verify.
    static void Main()
    {
        // Build the sample state first, then let the later output confirm the behavior step by step.
        Temperature temperature = new Temperature(-500.0);
        // Print the observed state here so learners can connect the code path to a concrete result.
        Console.WriteLine($"Initial value (clamped): {temperature.Celsius} C");

        bool updated = temperature.SetCelsius(25.0);
        Console.WriteLine($"Set to 25.0 success: {updated}");
        Console.WriteLine($"Current value: {temperature.Celsius} C");

        bool rejected = temperature.SetCelsius(-300.0);
        Console.WriteLine($"Set to -300.0 success: {rejected}");

        Console.WriteLine($"Current value: {temperature.Celsius} C");
    }
}
