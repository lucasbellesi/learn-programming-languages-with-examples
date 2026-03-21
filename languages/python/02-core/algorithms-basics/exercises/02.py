n = int(input("How many integers? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for index in range(n):
        values.append(int(input(f"Value {index + 1}: ")))

    min_value = values[0]
    max_value = values[0]
    even_count = 0

    for value in values:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
        if value % 2 == 0:
            even_count += 1

    print(f"Minimum: {min_value}")
    print(f"Maximum: {max_value}")
    print(f"Even numbers: {even_count}")
