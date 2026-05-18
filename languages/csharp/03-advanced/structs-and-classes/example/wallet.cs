// Module focus: Use a class to protect state behind behavior.
// Why it matters: classes are useful when data changes through controlled operations.

using System;

class Wallet
{
    private readonly string owner;
    private decimal balance;

    public Wallet(string ownerName, decimal initialBalance)
    {
        owner = string.IsNullOrWhiteSpace(ownerName) ? "Unknown" : ownerName.Trim();

        balance = initialBalance < 0m ? 0m : initialBalance;
    }

    public bool Deposit(decimal amount)
    {
        if (amount <= 0m)
        {
            return false;
        }

        balance += amount;
        return true;
    }

    public bool Withdraw(decimal amount)
    {
        if (amount <= 0m || amount > balance)
        {
            return false;
        }

        balance -= amount;
        return true;
    }

    public string Owner => owner;
    public decimal Balance => balance;
}
