n = int(input("How many numbers? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for _ in range(n):
        values.append(int(input()))

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if values[j] < values[min_index]:
                min_index = j

        values[i], values[min_index] = values[min_index], values[i]

    print(" ".join(str(value) for value in values))
