# This example shows storing related values in ordered collections and iterating safely.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
fixed_scores = [72, 88, 95]
# Print the observed state here so learners can match the code path to the result.
print("Fixed list values:", ", ".join(str(score) for score in fixed_scores))

count = int(input("How many temperatures do you want to enter? "))
if count <= 0:
    print("Nothing to process.")
else:
    temperatures = []
    for index in range(count):
        value = float(input(f"Temperature {index + 1}: "))
        temperatures.append(value)

    average = sum(temperatures) / len(temperatures)

    print("\nYou entered:", ", ".join(str(value) for value in temperatures))
    print(f"Average temperature: {average:.2f}")
