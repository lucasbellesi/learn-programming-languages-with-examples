# Module focus: Reordering data and locating values with deliberate search logic.
# Why it matters: practicing sorting and searching patterns makes exercises and checkpoints easier
# to reason about.

# Helper setup for sorting and searching; this keeps the walkthrough readable.
def binary_search(values, target):
    # Prepare sample inputs that exercise the key sorting and searching path.
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


# Walk through one fixed scenario so sorting and searching behavior stays repeatable.
def main():
    values = [7, 2, 9, 4, 2, 8]
    values.sort()

    # Report output values so learners can verify the sorting and searching outcome.
    print(f"Sorted: {' '.join(str(value) for value in values)}")

    target = 4
    index = binary_search(values, target)

    if index >= 0:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
