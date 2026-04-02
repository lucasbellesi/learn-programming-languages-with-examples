# This example shows rejecting invalid input before the main workflow continues.
# In Python, the example favors direct readable steps while keeping validation visible.

# Define the reusable pieces first so the main flow can focus on one observable scenario.
def read_int_in_range(prompt, min_value, max_value):
    # Build the sample state first, then let the later output confirm the behavior step by step.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input type. Please enter an integer.")
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
            print("Invalid input type. Please enter a decimal number.")
            continue

        if value < min_value or value > max_value:
            print(f"Value must be between {min_value} and {max_value}.")
            continue

        return value


# Run one deterministic scenario so the console output makes rejecting invalid input before the main
# workflow continues easy to verify.
def main():
    age = read_int_in_range("Enter your age (1-120): ", 1, 120)
    gpa = read_float_in_range("Enter your GPA (0.0-4.0): ", 0.0, 4.0)

    print("\nValidated input summary:")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")


if __name__ == "__main__":
    main()
