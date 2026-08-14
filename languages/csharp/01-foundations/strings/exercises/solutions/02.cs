using System;
using System.Text;

class Program
{
    static void Main()
    {
        Console.Write("Enter text: ");
        string line = Console.ReadLine() ?? "";

        StringBuilder normalizedBuilder = new StringBuilder();
        foreach (char ch in line)
        {
            if (char.IsLetter(ch))
            {
                normalizedBuilder.Append(char.ToLowerInvariant(ch));
            }
        }

        string normalized = normalizedBuilder.ToString();

        if (normalized.Length == 0)
        {
            Console.WriteLine("No letters to evaluate.");
            return;
        }

        bool isPalindrome = true;
        int left = 0;
        int right = normalized.Length - 1;

        while (left < right)
        {
            if (normalized[left] != normalized[right])
            {
                isPalindrome = false;
                break;
            }
            left++;
            right--;
        }

        Console.WriteLine(isPalindrome ? "Palindrome" : "Not palindrome");
    }
}
