# Module focus: Combining values through expressions and readable calculations.
# Why it matters: the example makes it possible to build expressions with correct precedence
# and explicit intent before the learner tackles the exercises.

# Fixed inputs make the consequence of forgetting to reject negative totals for time conversion or
# subtotal visible and repeatable.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# The printed result shows whether the program can distinguish arithmetic, comparison, and logical
# operations.
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
