from typing import TypeVar

TNumber = TypeVar("TNumber", int, float)


def average_of(values: list[TNumber]) -> float:
    if not values:
        return 0.0
    return sum(float(value) for value in values) / len(values)


raw_count = input("How many numbers? ").strip()
try:
    count = int(raw_count)
except ValueError:
    print("Please enter zero or a positive count.")
else:
    if count < 0:
        print("Please enter zero or a positive count.")
    else:
        values: list[float] = []
        valid = True
        for _ in range(count):
            raw_value = input().strip()
            try:
                values.append(float(raw_value))
            except ValueError:
                print("Invalid number.")
                valid = False
                break

        if valid:
            print(f"Average: {average_of(values)}")
