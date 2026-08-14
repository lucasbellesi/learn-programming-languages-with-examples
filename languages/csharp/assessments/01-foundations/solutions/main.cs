using System;
using System.Collections.Generic;

class Student
{
    public string Name { get; set; } = string.Empty;
    public int Score { get; set; }
}

class Program
{
    static int ReadPositiveCount()
    {
        while (true)
        {
            Console.Write("How many students? ");
            if (!int.TryParse(Console.ReadLine(), out int count))
            {
                Console.WriteLine("Invalid number. Try again.");
                continue;
            }

            if (count <= 0)
            {
                Console.WriteLine("Please enter a positive number.");
                continue;
            }

            return count;
        }
    }

    static int ReadScore(string studentName)
    {
        while (true)
        {
            Console.Write($"Score for {studentName} (0-100): ");
            if (!int.TryParse(Console.ReadLine(), out int score))
            {
                Console.WriteLine("Invalid score. Enter a number from 0 to 100.");
                continue;
            }

            if (score < 0 || score > 100)
            {
                Console.WriteLine("Score out of range. Enter a value from 0 to 100.");
                continue;
            }

            return score;
        }
    }

    static void Main()
    {
        int count = ReadPositiveCount();
        List<Student> students = new List<Student>(count);

        for (int index = 0; index < count; index++)
        {
            Console.Write($"Student name {index + 1}: ");
            string name = Console.ReadLine() ?? string.Empty;
            students.Add(new Student { Name = name, Score = ReadScore(name) });
        }

        int total = 0;
        int passCount = 0;
        int highestIndex = 0;
        int lowestIndex = 0;

        for (int index = 0; index < students.Count; index++)
        {
            total += students[index].Score;
            if (students[index].Score >= 60)
            {
                passCount++;
            }
            if (students[index].Score > students[highestIndex].Score)
            {
                highestIndex = index;
            }
            if (students[index].Score < students[lowestIndex].Score)
            {
                lowestIndex = index;
            }
        }

        double average = (double)total / students.Count;

        Console.WriteLine();
        Console.WriteLine("Students:");
        foreach (Student student in students)
        {
            Console.WriteLine($"- {student.Name}: {student.Score}");
        }

        Console.WriteLine($"Average: {average}");
        Console.WriteLine(
            $"Highest: {students[highestIndex].Name} ({students[highestIndex].Score})"
        );
        Console.WriteLine($"Lowest: {students[lowestIndex].Name} ({students[lowestIndex].Score})");
        Console.WriteLine($"Passed: {passCount}/{students.Count}");
    }
}
