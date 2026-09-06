# Read console text, convert numeric fields, and print a student summary.
# This first example assumes valid input; input-validation teaches error recovery.

# input() returns text; int() and float() convert it and can raise ValueError.
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# Print GPA with two decimal places and derive adulthood from the numeric age.
print("\n--- Student Summary ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
print(f"Adult: {age >= 18}")
