# This example demonstrates control flow concepts.

value = int(input("Enter an integer: "))

if value > 0:
    print("positive")
elif value < 0:
    print("negative")
else:
    print("zero")

n = int(input("Enter N: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"factorial({n}) = {factorial}")
print("Numbers 1..N:")
for i in range(1, n + 1):
    print(i)
