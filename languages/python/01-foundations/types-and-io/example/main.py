# This example demonstrates types and io concepts.

full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

print("\n--- Student Summary ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
print(f"Adult: {age >= 18}")
