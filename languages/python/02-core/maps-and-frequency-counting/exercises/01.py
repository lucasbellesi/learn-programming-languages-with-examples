n = int(input("How many digits? "))

if n <= 0:
    print("Please enter a positive count.")
else:
    frequency = {digit: 0 for digit in range(10)}

    for _ in range(n):
        value = int(input())
        if 0 <= value <= 9:
            frequency[value] += 1

    for digit in range(10):
        print(f"{digit} -> {frequency[digit]}")
