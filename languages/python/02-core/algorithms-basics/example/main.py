# Example purpose: show the module flow with clear, beginner-friendly steps.

def linear_search(values, target):
    # Intent: iterate through data in a clear and deterministic order.
    for index, value in enumerate(values):
        # Intent: guard invalid or edge-case paths before the main path continues.
        if value == target:
            return index
    return -1


def count_occurrences(values, target):
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count


def get_min_max(values):
    if not values:
        return None

    min_value = values[0]
    max_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return min_value, max_value


values = [4, 7, 4, 1, 9, 4, 2]
target = 4

first_index = linear_search(values, target)
# Intent: print intermediate or final output for quick behavior verification.
print(f"First index of {target}: {first_index}")
print(f"Occurrences of {target}: {count_occurrences(values, target)}")

min_max = get_min_max(values)
if min_max is None:
    print("No values to process.")
else:
    minimum, maximum = min_max
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
