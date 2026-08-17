// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: the example makes it possible to construct objects only in valid states before
// the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to construct objects only in valid states.
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
    // Fixed inputs make the consequence of accepting invalid constructor values and fixing later
    // visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        Temperature temperature = new Temperature(-500.0);
        // The printed result shows whether the program can keep mutations from violating
        // established invariants.
        Console.WriteLine($"Initial value (clamped): {temperature.Celsius} C");

        bool updated = temperature.SetCelsius(25.0);
        Console.WriteLine($"Set to 25.0 success: {updated}");
        Console.WriteLine($"Current value: {temperature.Celsius} C");

        bool rejected = temperature.SetCelsius(-300.0);
        Console.WriteLine($"Set to -300.0 success: {rejected}");

        Console.WriteLine($"Current value: {temperature.Celsius} C");
    }
}
