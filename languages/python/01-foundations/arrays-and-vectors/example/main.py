# This example demonstrates arrays and vectors concepts.

fixed_scores = [72, 88, 95]
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
