# Module focus: Guarding risky inputs so failures stay explicit and controlled.
# Why it matters: practicing error handling and defensive programming patterns makes exercises and
# checkpoints easier to reason about.

# Helper setup for error handling and defensive programming; this keeps the walkthrough readable.
def safe_divide(left, right):
    # Prepare sample inputs that exercise the key error handling and defensive programming path.
    if right == 0.0:
        return None
    return left / right


# Walk through one fixed scenario so error handling and defensive programming behavior stays
# repeatable.
def main():
    scenarios = [(42.0, 6.0), (10.0, 0.0)]

    for left, right in scenarios:
        # Report output values so learners can verify the error handling and defensive programming
        # outcome.
        print(f"Input: {left} {right}")

        quotient = safe_divide(left, right)
        if quotient is None:
            print("Cannot divide by zero.")
            continue

        print(f"Result: {quotient}")


if __name__ == "__main__":
    main()
