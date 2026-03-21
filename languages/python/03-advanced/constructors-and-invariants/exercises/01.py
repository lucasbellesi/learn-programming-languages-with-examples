class BankAccount:
    def __init__(self, initial_balance: float) -> None:
        self._balance = max(0.0, initial_balance)

    def deposit(self, amount: float) -> bool:
        if amount <= 0.0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0.0 or amount > self._balance:
            return False

        self._balance -= amount
        return True

    @property
    def balance(self) -> float:
        return self._balance


raw_initial = input("Initial balance: ").strip()
try:
    initial_balance = float(raw_initial)
except ValueError:
    print("Invalid initial balance.")
else:
    account = BankAccount(initial_balance)

    raw_deposit = input("Deposit amount: ").strip()
    try:
        account.deposit(float(raw_deposit))
    except ValueError:
        pass

    raw_withdraw = input("Withdraw amount: ").strip()
    try:
        withdraw_amount = float(raw_withdraw)
    except ValueError:
        withdraw_amount = None

    if withdraw_amount is not None and not account.withdraw(withdraw_amount):
        print("Withdrawal rejected.")

    print(f"Final balance: {account.balance}")
