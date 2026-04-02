# This example shows combining values through expressions and readable calculations.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Print the observed state here so learners can match the code path to the result.
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
