# Module focus: Reordering data and locating values with deliberate search logic.
# Why it matters: the example makes it possible to choose and apply sorting and searching
# operations correctly before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to choose and apply sorting and searching
# operations correctly.
def binary_search(values, target):
    # These values exercise the normal path before the exercises vary the documented boundaries.
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


# Fixed inputs make the consequence of running binary search on unsorted input visible and
# repeatable.
def main():
    values = [7, 2, 9, 4, 2, 8]
    values.sort()

    # The printed result shows whether the program can explain ordering, duplicates, missing
    # values, and stability tradeoffs.
    print(f"Sorted: {' '.join(str(value) for value in values)}")

    target = 4
    index = binary_search(values, target)

    if index >= 0:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
