using System;

class BankAccount
{
    private double balance;

    public BankAccount(double initialBalance)
    {
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

    public double Balance => balance;
}

class Program
{
    static void Main()
    {
        Console.Write("Initial balance: ");
        if (!double.TryParse(Console.ReadLine(), out double initialBalance))
        {
            Console.WriteLine("Invalid initial balance.");
            return;
        }

        BankAccount account = new BankAccount(initialBalance);

        Console.Write("Deposit amount: ");
        if (double.TryParse(Console.ReadLine(), out double depositAmount))
        {
            account.Deposit(depositAmount);
        }

        Console.Write("Withdraw amount: ");
        if (double.TryParse(Console.ReadLine(), out double withdrawAmount))
        {
            if (!account.Withdraw(withdrawAmount))
            {
                Console.WriteLine("Withdrawal rejected.");
            }
        }

        Console.WriteLine($"Final balance: {account.Balance}");
    }
}
