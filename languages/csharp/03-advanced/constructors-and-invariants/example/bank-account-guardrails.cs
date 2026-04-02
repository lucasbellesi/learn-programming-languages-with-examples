// This helper example focuses on showing how helper methods preserve invariants around deposits and withdrawals.

// This extra example extends constructors and invariants with a bank account.

using System;

// Keep this helper separate so the main example can focus on the larger idea without extra noise.
class BankAccount
{
    private readonly string owner;
    private double balance;

    public BankAccount(string ownerValue, double initialBalance)
    {
        owner = ownerValue.Trim().Length == 0 ? "Unknown" : ownerValue.Trim();
        balance = initialBalance < 0.0 ? 0.0 : initialBalance;
    }

    public bool Deposit(double amount)
    {
        if (amount <= 0.0)
        {
            return false;
        }

        balance += amount;
        return true;
    }

    public bool Withdraw(double amount)
    {
        if (amount <= 0.0 || amount > balance)
        {
            return false;
        }

        balance -= amount;
        return true;
    }

    public string Summary => $"{owner}: {balance:F2}";
}

class Program
{
    static void Main()
    {
        BankAccount account = new BankAccount("  Ana  ", -50.0);
        Console.WriteLine($"Initial: {account.Summary}");
        Console.WriteLine($"Deposit 20 success: {account.Deposit(20.0)}");
        Console.WriteLine($"Withdraw 10 success: {account.Withdraw(10.0)}");
        Console.WriteLine($"Withdraw 99 success: {account.Withdraw(99.0)}");
        Console.WriteLine($"Final: {account.Summary}");
    }
}
