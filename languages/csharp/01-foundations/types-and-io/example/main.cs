// Module focus: Representing values with suitable types and printing readable results.
// Why it matters: converting values explicitly makes calculations and output predictable.
// Read console text, convert numeric fields, and print a student summary.
// This first example assumes valid input; input-validation teaches TryParse.

using System;

class Program
{
    static void Main()
    {
        // ReadLine returns text; Parse converts it and can throw on invalid numeric input.
        // Decimal parsing and formatting use the current system culture.
        Console.Write("Enter your full name: ");
        string fullName = Console.ReadLine() ?? "";

        Console.Write("Enter your age: ");
        int age = int.Parse(Console.ReadLine() ?? "0");

        Console.Write("Enter your GPA: ");
        double gpa = double.Parse(Console.ReadLine() ?? "0");

        // Print GPA to two decimal places and derive adulthood from the numeric age.
        Console.WriteLine("\n--- Student Summary ---");
        Console.WriteLine($"Name: {fullName}");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
        Console.WriteLine($"Adult: {age >= 18}");
    }
}
