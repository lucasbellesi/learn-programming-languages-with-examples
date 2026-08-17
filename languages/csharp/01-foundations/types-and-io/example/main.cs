// Module focus: Reading typed input carefully and turning raw text into values.
// Why it matters: the example makes it possible to choose suitable primitive values and variables
// for a small problem before the learner tackles the exercises.

using System;

// Separate helpers keep the main path focused on how to choose suitable primitive values and
// variables for a small problem.
class Program
{
    // Fixed inputs make the consequence of assuming input parsing always succeeds without
    // validation visible and repeatable.
    static void Main()
    {
        // These values exercise the normal path before the exercises vary the documented
        // boundaries.
        // The printed result shows whether the program can read, validate, transform, and present
        // console data.
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
