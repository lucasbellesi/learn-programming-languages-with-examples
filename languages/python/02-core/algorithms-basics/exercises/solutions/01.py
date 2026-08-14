n = int(input("How many integers? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for index in range(n):
        values.append(int(input(f"Value {index + 1}: ")))

    target = int(input("Target to find: "))

    first_index = -1
    for index, value in enumerate(values):
        if value == target:
            first_index = index
            break

    print(f"First index: {first_index}")
