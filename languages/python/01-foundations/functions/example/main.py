# Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
# Why it matters: the example makes it possible to decompose a problem into focused functions with
# explicit contracts before the learner tackles the exercises.
# about.

# Separate helpers keep the main path focused on how to decompose a problem into focused functions
# with explicit contracts.
def add(a, b):
    return a + b


def swap_in_list(values, i, j):
    values[i], values[j] = values[j], values[i]


def print_list(values):
    print(values)


# Fixed inputs make the consequence of embedding all logic in main instead of reusable helpers
# visible and repeatable.
# The printed result shows whether the program can use parameters and return values without hidden
# state changes.
print(add(4, 6))

numbers = [10, 20, 30]
print_list(numbers)
swap_in_list(numbers, 0, 1)
print_list(numbers)
