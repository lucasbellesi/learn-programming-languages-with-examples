# This extra example extends types-and-io with a validation loop.
# Example purpose: show how string input and numeric checks work together.

full_name = input("Enter your full name: ").strip()

while True:
    raw_age = input("Enter your age (1-120): ").strip()
    try:
        age = int(raw_age)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if age < 1 or age > 120:
        print("Age must be between 1 and 120.")
        continue

    break

print("\nRegistration summary:")
print(f"Name: {full_name}")
print(f"Age: {age}")
