values_line = input("Enter numeric values separated by spaces: ").strip()

if not values_line:
    print("No values entered.")
else:
    values = [float(token) for token in values_line.split()]
    precision = int(input("Decimal precision (0-6): "))

    if precision < 0 or precision > 6:
        print("Precision must be between 0 and 6.")
    else:
        total = sum(values)
        average = total / len(values)
        minimum = min(values)
        maximum = max(values)
        fmt = f"{{:.{precision}f}}"

        print(f"Count: {len(values)}")
        print(f"Sum: {fmt.format(total)}")
        print(f"Average: {fmt.format(average)}")
        print(f"Minimum: {fmt.format(minimum)}")
        print(f"Maximum: {fmt.format(maximum)}")
