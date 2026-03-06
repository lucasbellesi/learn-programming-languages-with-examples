n = int(input("How many numbers? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for i in range(n):
        values.append(float(input(f"Value {i + 1}: ")))

    total = sum(values)
    average = total / n
    minimum = min(values)
    maximum = max(values)

    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
