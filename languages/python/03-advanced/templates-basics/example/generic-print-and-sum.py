# This extra example extends templates-basics with reusable typed helpers.
# Example purpose: print sequences and sum numeric values with one shared implementation.

from typing import TypeVar

T = TypeVar("T")
N = TypeVar("N", int, float)


def print_list(values: list[T], label: str) -> None:
    print(f"{label}: [{', '.join(str(value) for value in values)}]")


def sum_list(values: list[N]) -> N:
    total = values[0] * 0 if values else 0
    for value in values:
        total += value
    return total


numbers = [2, 4, 6, 8]
prices = [1.5, 2.25, 3.75]

print_list(numbers, "Numbers")
print_list(prices, "Prices")

print(f"Sum of numbers: {sum_list(numbers)}")
print(f"Sum of prices: {sum_list(prices)}")
