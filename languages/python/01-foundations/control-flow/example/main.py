# Module focus: Choosing between branches and repeating work with predictable control flow.
# Why it matters: practicing control flow patterns makes exercises and checkpoints easier to reason
# about.

# Walk through one fixed scenario so control flow behavior stays repeatable.
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

# Report values so learners can verify the control flow outcome.
print(f"factorial({n}) = {factorial}")
print("Numbers 1..N:")
for i in range(1, n + 1):
    print(i)
