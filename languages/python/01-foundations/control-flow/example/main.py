# Module focus: Choosing between branches and repeating work with predictable control flow.
# Why it matters: the example makes it possible to select branches that cover normal and boundary
# conditions before the learner tackles the exercises.
# about.

# Fixed inputs make the consequence of not handling non-positive upper bounds before entering
# loops visible and repeatable.
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

# The printed result shows whether the program can write terminating loops and reason about their
# invariants.
print(f"factorial({n}) = {factorial}")
print("Numbers 1..N:")
for i in range(1, n + 1):
    print(i)
