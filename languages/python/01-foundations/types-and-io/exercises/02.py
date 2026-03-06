parts = input("Enter product price quantity: ").split()

if len(parts) != 3:
    print("Invalid format. Use: product price quantity")
else:
    product = parts[0]
    price = float(parts[1])
    quantity = int(parts[2])
    total = price * quantity

    print(f"Product: {product}")
    print(f"Total price: {total}")
