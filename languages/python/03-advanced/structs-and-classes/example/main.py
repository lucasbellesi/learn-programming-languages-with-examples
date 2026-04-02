# Module focus: Modeling related data and behavior with structured types.
# Why it matters: practicing structs and classes patterns makes exercises and checkpoints easier to
# reason about.

from dataclasses import dataclass


# Prepare sample inputs that exercise the key structs and classes path.
@dataclass(frozen=True)
# Helper setup for structs and classes; this keeps the walkthrough readable.
class Coordinate:
    x: int
    y: int

    def manhattan_distance_from_origin(self) -> int:
        return abs(self.x) + abs(self.y)


class Wallet:
    def __init__(self, owner: str, initial_balance: float) -> None:
        clean_owner = owner.strip() if owner.strip() else "Unknown"

        self._owner = clean_owner
        self._balance = max(0.0, initial_balance)

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            return False

        self._balance += amount
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0 or amount > self._balance:
            return False

        self._balance -= amount
        return True

    @property
    def owner(self) -> str:
        return self._owner

    @property
    def balance(self) -> float:
        return self._balance


# Walk through one fixed scenario so structs and classes behavior stays repeatable.
def main() -> None:
    route = [Coordinate(2, 3), Coordinate(-1, 4), Coordinate(5, -2)]

    # Report output values so learners can verify the structs and classes outcome.
    print("Coordinates (dataclass example):")
    for point in route:
        print(
            f"Point ({point.x}, {point.y}), "
            f"Manhattan distance = {point.manhattan_distance_from_origin()}"
        )

    wallet = Wallet("Maya", 120.0)
    wallet.deposit(35.0)
    wallet.withdraw(40.0)

    print("\nWallet (class example):")
    print(f"Owner: {wallet.owner}")
    print(f"Balance: {wallet.balance:.2f}")


if __name__ == "__main__":
    main()
