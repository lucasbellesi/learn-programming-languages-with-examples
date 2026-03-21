# This example demonstrates types and io concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

# Intent: gather typed input first so later operations are predictable.
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# Intent: print intermediate or final output for quick behavior verification.
print("\n--- Student Summary ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
print(f"Adult: {age >= 18}")
