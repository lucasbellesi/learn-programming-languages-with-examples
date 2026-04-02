# Module focus: Reading typed input carefully and turning raw text into values.
# Why it matters: practicing types and io patterns makes exercises and checkpoints easier to reason
# about.

# Walk through one fixed scenario so types and io behavior stays repeatable.
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# Report values so learners can verify the types and io outcome.
print("\n--- Student Summary ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
print(f"Adult: {age >= 18}")
