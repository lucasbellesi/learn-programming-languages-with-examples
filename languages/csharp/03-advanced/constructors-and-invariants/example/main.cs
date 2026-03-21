// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Temperature
{
    private double celsius;

    public Temperature(double celsiusValue)
    {
        // Intent: enforce the invariant at construction time.
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
    static void Main()
    {
        // Program flow: construct with invalid input, then apply valid and invalid updates.
        Temperature temperature = new Temperature(-500.0);
        Console.WriteLine($"Initial value (clamped): {temperature.Celsius} C");

        bool updated = temperature.SetCelsius(25.0);
        Console.WriteLine($"Set to 25.0 success: {updated}");
        Console.WriteLine($"Current value: {temperature.Celsius} C");

        bool rejected = temperature.SetCelsius(-300.0);
        Console.WriteLine($"Set to -300.0 success: {rejected}");

        // Intent: final state confirms that invariant was preserved.
        Console.WriteLine($"Current value: {temperature.Celsius} C");
    }
}
