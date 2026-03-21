while True:
    raw = input("Enter two numbers to divide (a b): ").strip()
    parts = raw.split()

    if len(parts) != 2:
        print("Invalid input type. Try again.")
        continue

    try:
        a = float(parts[0])
        b = float(parts[1])
    except ValueError:
        print("Invalid input type. Try again.")
        continue

    if b == 0.0:
        print("Divisor cannot be zero. Try again.")
        continue

    print(f"Result: {a / b}")
    break
