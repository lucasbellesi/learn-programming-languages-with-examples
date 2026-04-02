// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for constructors and invariants; this keeps the walkthrough readable.
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
    // Walk through one fixed scenario so constructors and invariants behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key constructors and invariants path.
        Temperature temperature = new Temperature(-500.0);
        // Report values so learners can verify the constructors and invariants outcome.
        Console.WriteLine($"Initial value (clamped): {temperature.Celsius} C");

        bool updated = temperature.SetCelsius(25.0);
        Console.WriteLine($"Set to 25.0 success: {updated}");
        Console.WriteLine($"Current value: {temperature.Celsius} C");

        bool rejected = temperature.SetCelsius(-300.0);
        Console.WriteLine($"Set to -300.0 success: {rejected}");

        Console.WriteLine($"Current value: {temperature.Celsius} C");
    }
}
