from typing import TypeVar

T = TypeVar("T")


def swap_values(left: T, right: T) -> tuple[T, T]:
    return right, left


parts = input("Enter two integers: ").strip().split()
if len(parts) != 2:
    print("Invalid input.")
else:
    try:
        left_value = int(parts[0])
        right_value = int(parts[1])
    except ValueError:
        print("Invalid input.")
    else:
        print(f"Before swap: {left_value} {right_value}")
        left_value, right_value = swap_values(left_value, right_value)
        print(f"After swap: {left_value} {right_value}")
