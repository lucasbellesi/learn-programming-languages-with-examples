n = int(input("How many sorted values? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    values = []
    for _ in range(n):
        values.append(int(input()))

    target = int(input("Target: "))

    left = 0
    right = n - 1
    index = -1

    while left <= right:
        mid = left + (right - left) // 2
        mid_value = values[mid]

        if mid_value == target:
            index = mid
            break

        if mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Index: {index}")
