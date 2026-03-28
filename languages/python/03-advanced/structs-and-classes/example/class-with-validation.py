# This extra example extends structs-and-classes with validated object state.
# Example purpose: keep class invariants inside the constructor and methods.


class BankAccount:
    def __init__(self, owner, initial_balance):
        if not owner:
            raise ValueError("Owner name cannot be empty.")
        if initial_balance < 0.0:
            raise ValueError("Initial balance cannot be negative.")

        self._owner = owner
        self._balance = initial_balance

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
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance


try:
    account = BankAccount("Ana Smith", 100.0)

    print(f"Account owner: {account.owner}")
    print(f"Initial balance: {account.balance}")

    if account.deposit(50.0):
        print("Deposit successful.")

    if account.withdraw(30.0):
        print("Withdraw successful.")

    if not account.withdraw(500.0):
        print("Withdraw rejected (insufficient funds).")

    print(f"Final balance: {account.balance}")
except ValueError as error:
    print(f"Error: {error}")
