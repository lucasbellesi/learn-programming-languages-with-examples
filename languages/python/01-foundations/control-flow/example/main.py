# This example shows choosing between branches and repeating work with predictable control flow.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
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

# Print the observed state here so learners can match the code path to the result.
print(f"factorial({n}) = {factorial}")
print("Numbers 1..N:")
for i in range(1, n + 1):
    print(i)
