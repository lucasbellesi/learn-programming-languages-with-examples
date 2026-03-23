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
            int score = ReadScore(name);
            students.Add(new Student { Name = name, Score = score });
        }

        int minScore = students[0].Score;
        int maxScore = students[0].Score;
        int sum = 0;

        Console.WriteLine();
        Console.WriteLine("Students:");
        foreach (Student student in students)
        {
            Console.WriteLine($"- {student.Name}: {student.Score}");
            sum += student.Score;
            if (student.Score < minScore)
            {
                minScore = student.Score;
            }
            if (student.Score > maxScore)
            {
                maxScore = student.Score;
            }
        }

        double average = (double)sum / students.Count;
        Console.WriteLine($"Average: {average}");
        Console.WriteLine($"Minimum: {minScore}");
        Console.WriteLine($"Maximum: {maxScore}");
    }
}
