line = input("Enter integers separated by spaces: ").strip()

if not line:
    print("No values entered.")
else:
    values = [int(token) for token in line.split()]
    target = int(input("Target value: "))

    frequency = sum(1 for value in values if value == target)
    print(f"Frequency of {target}: {frequency}")
