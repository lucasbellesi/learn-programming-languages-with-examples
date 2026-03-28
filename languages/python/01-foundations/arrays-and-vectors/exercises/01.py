count = int(input("How many values? "))

if count <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for index in range(count):
        values.append(int(input(f"Value {index + 1}: ")))

    print("Values in reverse order:")
    for value in reversed(values):
        print(value)
