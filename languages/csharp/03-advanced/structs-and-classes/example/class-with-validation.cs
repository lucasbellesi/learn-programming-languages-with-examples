// This extra example extends structs-and-classes with validated object state.
// Example purpose: keep class invariants inside the constructor and methods.

using System;

class BankAccount
{
    public BankAccount(string ownerName, double initialBalance)
    {
        if (ownerName.Length == 0)
        {
            throw new ArgumentException("Owner name cannot be empty.");
        }

        if (initialBalance < 0.0)
        {
            throw new ArgumentException("Initial balance cannot be negative.");
        }

        Owner = ownerName;
        Balance = initialBalance;
    }

    public string Owner { get; }

    public double Balance { get; private set; }

    public bool Deposit(double amount)
    {
        if (amount <= 0.0)
        {
            return false;
        }

        Balance += amount;
        return true;
    }

    public bool Withdraw(double amount)
    {
        if (amount <= 0.0 || amount > Balance)
        {
            return false;
        }

        Balance -= amount;
        return true;
    }
}

class Program
{
    static void Main()
    {
        try
        {
            BankAccount account = new BankAccount("Ana Smith", 100.0);

            Console.WriteLine($"Account owner: {account.Owner}");
            Console.WriteLine($"Initial balance: {account.Balance}");

            if (account.Deposit(50.0))
            {
                Console.WriteLine("Deposit successful.");
            }

            if (account.Withdraw(30.0))
            {
                Console.WriteLine("Withdraw successful.");
            }

            if (!account.Withdraw(500.0))
            {
                Console.WriteLine("Withdraw rejected (insufficient funds).");
            }

            Console.WriteLine($"Final balance: {account.Balance}");
        }
        catch (ArgumentException error)
        {
            Console.WriteLine($"Error: {error.Message}");
        }
    }
}
