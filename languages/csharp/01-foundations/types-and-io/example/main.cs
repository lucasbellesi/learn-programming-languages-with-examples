// This example demonstrates types and io concepts.
// Example purpose: show the module flow with clear, beginner-friendly steps.

using System;

class Program
{
    static void Main()
    {
        // Program flow: collect input, apply core logic, then print a verifiable result.
        // Intent: print intermediate or final output for quick behavior verification.
        Console.Write("Enter your full name: ");
        // Intent: gather typed input first so later operations are predictable.
        string fullName = Console.ReadLine() ?? "";

        Console.Write("Enter your age: ");
        int age = int.Parse(Console.ReadLine() ?? "0");

        Console.Write("Enter your GPA: ");
        double gpa = double.Parse(Console.ReadLine() ?? "0");

        Console.WriteLine("\n--- Student Summary ---");
        Console.WriteLine($"Name: {fullName}");
        Console.WriteLine($"Age: {age}");
        Console.WriteLine($"GPA: {gpa:F2}");
        Console.WriteLine($"Adult: {age >= 18}");
    }
}
