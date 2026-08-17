# Module focus: Guarding risky inputs so failures stay explicit and controlled.
# Why it matters: the example makes it possible to separate expected failures from
# programming defects before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to separate expected failures from
# programming defects.
def safe_divide(left, right):
    # These values exercise the normal path before the exercises vary the documented boundaries.
    if right == 0.0:
        return None
    return left / right


# A fixed scenario makes the main decision path visible and repeatable.
def main():
    scenarios = [(42.0, 6.0), (10.0, 0.0)]

    for left, right in scenarios:
        # The printed result shows whether the program can preserve valid state and useful
        # diagnostics when operations fail.
        print(f"Input: {left} {right}")

        quotient = safe_divide(left, right)
        if quotient is None:
            print("Cannot divide by zero.")
            continue

        print(f"Result: {quotient}")


if __name__ == "__main__":
    main()
