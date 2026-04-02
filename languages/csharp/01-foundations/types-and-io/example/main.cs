// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: practicing types and io patterns makes exercises and checkpoints easier to reason about.

using System;

// Helper setup for types and io; this keeps the walkthrough readable.
class Program
{
    // Walk through one fixed scenario so types and io behavior stays repeatable.
    static void Main()
    {
        // Prepare sample inputs that exercise the key types and io path.
        // Report values so learners can verify the types and io outcome.
        Console.Write("Enter your full name: ");
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
