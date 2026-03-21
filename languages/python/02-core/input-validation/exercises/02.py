def read_int_in_range(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value


def read_float_in_range(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value


count = read_int_in_range("How many scores (1-50)? ", 1, 50)

total = 0.0
for index in range(count):
    score = read_float_in_range(f"Score {index + 1} (0-100): ", 0.0, 100.0)
    total += score

print(f"Average score: {total / count}")
