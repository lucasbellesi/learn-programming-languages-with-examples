# This example shows reordering data and locating values with deliberate search logic.
# In Python, the example favors direct readable steps while keeping validation visible.

# Define the reusable pieces first so the main flow can focus on one observable scenario.
def binary_search(values, target):
    # Build the sample state first, then let the later output confirm the behavior step by step.
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = values[mid]

        if mid_value == target:
            return mid

        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Run one deterministic scenario so the console output makes reordering data and locating values
# with deliberate search logic easy to verify.
def main():
    values = [7, 2, 9, 4, 2, 8]
    values.sort()

    print(f"Sorted: {' '.join(str(value) for value in values)}")

    target = 4
    index = binary_search(values, target)

    if index >= 0:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
