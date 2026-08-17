# Module focus: Reading typed input carefully and turning raw text into values.
# Why it matters: the example makes it possible to choose suitable primitive values and variables
# for a small problem before the learner tackles the exercises.
# about.

# Fixed inputs make the consequence of assuming input parsing always succeeds without validation
# visible and repeatable.
full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
gpa = float(input("Enter your GPA: "))

# The printed result shows whether the program can read, validate, transform, and present console
# data.
print("\n--- Student Summary ---")
print(f"Name: {full_name}")
print(f"Age: {age}")
print(f"GPA: {gpa:.2f}")
print(f"Adult: {age >= 18}")
