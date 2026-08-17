# Module focus: Modeling related data and behavior with structured types.
# Why it matters: the example makes it possible to model data and behavior with cohesive domain
# types before the learner tackles the exercises.

from dataclasses import dataclass


# These values exercise the normal path before the exercises vary the documented boundaries.
@dataclass(frozen=True)
# Separate helpers keep the main path focused on how to model data and behavior with cohesive
# domain types.
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


# Fixed inputs make the consequence of placing mutable shared defaults directly on class
# definitions visible and repeatable.
def main() -> None:
    route = [Coordinate(2, 3), Coordinate(-1, 4), Coordinate(5, -2)]

    # The printed result shows whether the program can protect invariants through constructors and
    # methods.
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
