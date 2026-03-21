# This example demonstrates arrays and vectors concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

fixed_scores = [72, 88, 95]
# Intent: print intermediate or final output for quick behavior verification.
print("Fixed list values:", ", ".join(str(score) for score in fixed_scores))

# Intent: gather typed input first so later operations are predictable.
count = int(input("How many temperatures do you want to enter? "))
# Intent: guard invalid or edge-case paths before the main path continues.
if count <= 0:
    print("Nothing to process.")
else:
    temperatures = []
    # Intent: iterate through data in a clear and deterministic order.
    for index in range(count):
        value = float(input(f"Temperature {index + 1}: "))
        temperatures.append(value)

    average = sum(temperatures) / len(temperatures)

    print("\nYou entered:", ", ".join(str(value) for value in temperatures))
    print(f"Average temperature: {average:.2f}")
