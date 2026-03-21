def read_int_in_range(prompt, min_value, max_value):
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if value < min_value or value > max_value:
            print("Out of range. Try again.")
            continue

        return value


value = read_int_in_range("Enter an integer from 1 to 100: ", 1, 100)
print(f"Square: {value * value}")
