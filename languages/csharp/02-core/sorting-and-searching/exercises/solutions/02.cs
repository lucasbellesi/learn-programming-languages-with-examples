using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.Write("How many sorted values? ");
        int n = int.Parse(Console.ReadLine() ?? "0");

        if (n <= 0)
        {
            Console.WriteLine("Please enter a positive count.");
            return;
        }

        List<int> values = new List<int>();
        for (int i = 0; i < n; i++)
        {
            values.Add(int.Parse(Console.ReadLine() ?? "0"));
        }

        Console.Write("Target: ");
        int target = int.Parse(Console.ReadLine() ?? "0");

        int left = 0;
        int right = n - 1;
        int index = -1;

        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            int midValue = values[mid];

            if (midValue == target)
            {
                index = mid;
                break;
            }

            if (midValue < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }

        Console.WriteLine($"Index: {index}");
    }
}
