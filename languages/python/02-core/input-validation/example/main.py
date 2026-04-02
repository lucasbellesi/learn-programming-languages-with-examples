# Module focus: Rejecting invalid input before the main workflow continues.
# Why it matters: practicing input validation patterns makes exercises and checkpoints easier to
# reason about.

# Helper setup for input validation; this keeps the walkthrough readable.
def read_int_in_range(prompt, min_value, max_value):
    # Prepare sample inputs that exercise the key input validation path.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            # Report output values so learners can verify the input validation outcome.
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


# Walk through one fixed scenario so input validation behavior stays repeatable.
def main():
    age = read_int_in_range("Enter your age (1-120): ", 1, 120)
    gpa = read_float_in_range("Enter your GPA (0.0-4.0): ", 0.0, 4.0)

    print("\nValidated input summary:")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")


if __name__ == "__main__":
    main()
