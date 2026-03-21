# This example demonstrates functions concepts.

def add(a, b):
    return a + b


def swap_in_list(values, i, j):
    values[i], values[j] = values[j], values[i]


def print_list(values):
    print(values)


print(add(4, 6))

numbers = [10, 20, 30]
print_list(numbers)
swap_in_list(numbers, 0, 1)
print_list(numbers)
