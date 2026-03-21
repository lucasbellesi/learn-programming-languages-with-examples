# This example demonstrates operators and expressions concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

# Intent: gather typed input first so later operations are predictable.
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Intent: print intermediate or final output for quick behavior verification.
print(f"Time: {hours}:{minutes:02d}:{seconds:02d}")

value_a = float(input("Enter first number: "))
value_b = float(input("Enter second number: "))

print(f"Sum: {value_a + value_b}")
print(f"Difference: {value_a - value_b}")
print(f"Product: {value_a * value_b}")

# Intent: guard invalid or edge-case paths before the main path continues.
if value_b != 0:
    print(f"Division: {value_a / value_b}")
    print(f"Floor division: {value_a // value_b}")
else:
    print("Division is not possible because second number is zero.")
