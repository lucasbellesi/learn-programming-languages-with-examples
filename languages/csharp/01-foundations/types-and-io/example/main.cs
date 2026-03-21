using System;

class Program
{
    static void Main()
    {
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
