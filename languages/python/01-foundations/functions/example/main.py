# Module focus: Breaking behavior into reusable functions with clear inputs and outputs.
# Why it matters: practicing functions patterns makes exercises and checkpoints easier to reason
# about.

# Helper setup for functions; this keeps the walkthrough readable.
def add(a, b):
    return a + b


def swap_in_list(values, i, j):
    values[i], values[j] = values[j], values[i]


def print_list(values):
    print(values)


# Walk through one fixed scenario so functions behavior stays repeatable.
# Report values so learners can verify the functions outcome.
print(add(4, 6))

numbers = [10, 20, 30]
print_list(numbers)
swap_in_list(numbers, 0, 1)
print_list(numbers)
