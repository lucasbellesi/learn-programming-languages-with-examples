# Module focus: Combining values through expressions and readable calculations.
# Why it matters: practicing operators and expressions patterns makes exercises and checkpoints
# easier to reason about.

# Walk through one fixed scenario so operators and expressions behavior stays repeatable.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Report values so learners can verify the operators and expressions outcome.
print(f"Time: {hours}:{minutes:02d}:{seconds:02d}")

value_a = float(input("Enter first number: "))
value_b = float(input("Enter second number: "))

print(f"Sum: {value_a + value_b}")
print(f"Difference: {value_a - value_b}")
print(f"Product: {value_a * value_b}")

if value_b != 0:
    print(f"Division: {value_a / value_b}")
    print(f"Floor division: {value_a // value_b}")
else:
    print("Division is not possible because second number is zero.")
