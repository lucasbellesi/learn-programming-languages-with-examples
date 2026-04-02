# This example shows guarding risky inputs so failures stay explicit and controlled.
# In Python, the example favors direct readable steps while keeping validation visible.

# Define the reusable pieces first so the main flow can focus on one observable scenario.
def safe_divide(left, right):
    # Build the sample state first, then let the later output confirm the behavior step by step.
    if right == 0.0:
        return None
    return left / right


# Run one deterministic scenario so the console output makes guarding risky inputs so failures stay
# explicit and controlled easy to verify.
def main():
    scenarios = [(42.0, 6.0), (10.0, 0.0)]

    for left, right in scenarios:
        print(f"Input: {left} {right}")

        quotient = safe_divide(left, right)
        if quotient is None:
            print("Cannot divide by zero.")
            continue

        print(f"Result: {quotient}")


if __name__ == "__main__":
    main()
