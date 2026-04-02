# This example shows walking data step by step to compute summaries and decisions.
# In Python, the example favors direct readable steps while keeping validation visible.


# Define the reusable pieces first so the later top-level flow stays easy to read.
def linear_search(values, target):
    for index, value in enumerate(values):
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


# Run one direct scenario at the top level so the printed result is easy to verify.
values = [4, 7, 4, 1, 9, 4, 2]
target = 4

first_index = linear_search(values, target)
# Print the observed state here so learners can match the code path to the result.
print(f"First index of {target}: {first_index}")
print(f"Occurrences of {target}: {count_occurrences(values, target)}")

min_max = get_min_max(values)
if min_max is None:
    print("No values to process.")
else:
    minimum, maximum = min_max
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
