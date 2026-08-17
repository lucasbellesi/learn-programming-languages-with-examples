# Module focus: Walking data step by step to compute summaries and decisions.
# Why it matters: the example makes it possible to implement linear scans and accumulations with
# clear invariants before the learner tackles the exercises.

# Separate helpers keep the main path focused on how to implement linear scans and accumulations
# with clear invariants.
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


# Fixed inputs make the consequence of forgetting to handle empty lists before min/max logic
# visible and repeatable.
values = [4, 7, 4, 1, 9, 4, 2]
target = 4

first_index = linear_search(values, target)
# The printed result shows whether the program can analyze behavior for empty, duplicate, and
# missing values.
print(f"First index of {target}: {first_index}")
print(f"Occurrences of {target}: {count_occurrences(values, target)}")

min_max = get_min_max(values)
if min_max is None:
    print("No values to process.")
else:
    minimum, maximum = min_max
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
