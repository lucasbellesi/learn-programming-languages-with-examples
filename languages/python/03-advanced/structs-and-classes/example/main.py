# Example purpose: show the module flow with clear, beginner-friendly steps.

from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def manhattan_distance_from_origin(self) -> int:
        return abs(self.x) + abs(self.y)


class Wallet:
    def __init__(self, owner: str, initial_balance: float) -> None:
        clean_owner = owner.strip() if owner.strip() else "Unknown"

        # Intent: normalize invalid starting values to preserve class invariants.
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


def main() -> None:
    # Program flow: inspect value-like objects, then apply class-based state changes.
    route = [Coordinate(2, 3), Coordinate(-1, 4), Coordinate(5, -2)]

    print("Coordinates (dataclass example):")
    # Intent: deterministic iteration helps beginners verify output quickly.
    for point in route:
        print(
            f"Point ({point.x}, {point.y}), "
            f"Manhattan distance = {point.manhattan_distance_from_origin()}"
        )

    wallet = Wallet("Maya", 120.0)
    wallet.deposit(35.0)
    wallet.withdraw(40.0)

    # Intent: report final state after guarded operations.
    print("\nWallet (class example):")
    print(f"Owner: {wallet.owner}")
    print(f"Balance: {wallet.balance:.2f}")


if __name__ == "__main__":
    main()
