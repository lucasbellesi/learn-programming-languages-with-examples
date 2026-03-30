using System;

sealed class Course
{
    private readonly string title;
    private readonly int capacity;
    private int enrolled;

    public Course(string titleValue, int capacityValue)
    {
        title = titleValue;
        capacity = capacityValue < 0 ? 0 : capacityValue;
        enrolled = 0;
    }

    public bool Enroll()
    {
        if (enrolled >= capacity)
        {
            return false;
        }

        enrolled++;
        return true;
    }

    public bool Drop()
    {
        if (enrolled <= 0)
        {
            return false;
        }

        enrolled--;
        return true;
    }

    public void PrintStatus()
    {
        Console.WriteLine($"Course: {title} | {enrolled}/{capacity} enrolled");
    }
}

class Program
{
    static void Main()
    {
        Course csharpBasics = new Course("CSharpBasics", 2);
        Course algorithms = new Course("Algorithms", 3);

        csharpBasics.Enroll();
        csharpBasics.Enroll();
        csharpBasics.Enroll();

        algorithms.Enroll();

        csharpBasics.PrintStatus();
        algorithms.PrintStatus();
    }
}
