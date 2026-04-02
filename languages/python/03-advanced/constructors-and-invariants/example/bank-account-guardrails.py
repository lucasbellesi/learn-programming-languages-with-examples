# This helper example focuses on showing how helper methods preserve invariants around deposits and
# withdrawals.

# This extra example extends constructors and invariants with a bank account.

# Keep this helper separate so the main example can focus on the larger idea without extra noise.
class BankAccount:
    def __init__(self, owner, initial_balance):
        self._owner = owner.strip() or "Unknown"
        self._balance = max(0.0, initial_balance)

    def deposit(self, amount):
        if amount <= 0.0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0.0 or amount > self._balance:
            return False

        self._balance -= amount
        return True

    @property
    def summary(self):
        return f"{self._owner}: {self._balance:.2f}"


account = BankAccount("  Ana  ", -50.0)
print(f"Initial: {account.summary}")
print(f"Deposit 20 success: {account.deposit(20.0)}")
print(f"Withdraw 10 success: {account.withdraw(10.0)}")
print(f"Withdraw 99 success: {account.withdraw(99.0)}")
print(f"Final: {account.summary}")
