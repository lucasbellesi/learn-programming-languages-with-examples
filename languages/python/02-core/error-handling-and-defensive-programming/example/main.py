# Example purpose: show the module flow with clear, beginner-friendly steps.


def safe_divide(left, right):
    # Intent: block invalid operations before performing division.
    if right == 0.0:
        return None
    return left / right


def main():
    # Program flow: run fixed scenarios to show both valid and invalid paths.
    scenarios = [(42.0, 6.0), (10.0, 0.0)]

    for left, right in scenarios:
        # Intent: print scenario input so behavior is easy to verify.
        print(f"Input: {left} {right}")

        quotient = safe_divide(left, right)
        if quotient is None:
            print("Cannot divide by zero.")
            continue

        # Intent: print deterministic final output for behavior verification.
        print(f"Result: {quotient}")


if __name__ == "__main__":
    main()
