# Example purpose: show the module flow with clear, beginner-friendly steps.


def binary_search(values, target):
    left = 0
    right = len(values) - 1

    # Intent: reduce the search interval based on sorted ordering.
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = values[mid]

        # Intent: return immediately when the target value is found.
        if mid_value == target:
            return mid

        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    # Program flow: sort values first, then search on the sorted list.
    values = [7, 2, 9, 4, 2, 8]
    values.sort()

    # Intent: print sorted data to verify the binary-search precondition.
    print(f"Sorted: {' '.join(str(value) for value in values)}")

    target = 4
    index = binary_search(values, target)

    # Intent: guard the not-found case explicitly.
    if index >= 0:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
