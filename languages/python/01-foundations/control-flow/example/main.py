# This example demonstrates control flow concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

# Intent: gather typed input first so later operations are predictable.
value = int(input("Enter an integer: "))

# Intent: guard invalid or edge-case paths before the main path continues.
if value > 0:
    # Intent: print intermediate or final output for quick behavior verification.
    print("positive")
elif value < 0:
    print("negative")
else:
    print("zero")

n = int(input("Enter N: "))

factorial = 1
# Intent: iterate through data in a clear and deterministic order.
for i in range(1, n + 1):
    factorial *= i

print(f"factorial({n}) = {factorial}")
print("Numbers 1..N:")
for i in range(1, n + 1):
    print(i)
