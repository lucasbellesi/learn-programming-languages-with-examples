# This example shows breaking behavior into reusable functions with clear inputs and outputs.
# In Python, the example favors direct readable steps while keeping validation visible.


# Define the reusable pieces first so the later top-level flow stays easy to read.
def add(a, b):
    return a + b


def swap_in_list(values, i, j):
    values[i], values[j] = values[j], values[i]


def print_list(values):
    print(values)


# Run one direct scenario at the top level so the printed result is easy to verify.
# Print the observed state here so learners can match the code path to the result.
print(add(4, 6))

numbers = [10, 20, 30]
print_list(numbers)
swap_in_list(numbers, 0, 1)
print_list(numbers)
