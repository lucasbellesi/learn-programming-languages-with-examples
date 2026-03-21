count = int(input("How many values? "))

if count <= 0:
    print("Please enter a positive count.")
else:
    total = 0
    for index in range(count):
        value = int(input(f"Value {index + 1}: "))
        total += value

    print(f"Sum: {total}")
    print(f"Average: {total / count:.2f}")
