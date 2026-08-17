# Module focus: Rejecting invalid input before the main workflow continues.
# Why it matters: the example makes it possible to reject malformed and out-of-domain input
# without corrupting state before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to reject malformed and out-of-domain input
# without corrupting state.
def read_int_in_range(prompt, min_value, max_value):
    # These values exercise the normal path before the exercises vary the documented boundaries.
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            # The printed result shows whether the program can design retry and termination
            # behavior that cannot loop accidentally.
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


# Fixed inputs make the consequence of calling `int()` or `float()` once and crashing on invalid
# input visible and repeatable.
def main():
    age = read_int_in_range("Enter your age (1-120): ", 1, 120)
    gpa = read_float_in_range("Enter your GPA (0.0-4.0): ", 0.0, 4.0)

    print("\nValidated input summary:")
    print(f"Age: {age}")
    print(f"GPA: {gpa}")


if __name__ == "__main__":
    main()
