products = []
count = int(input("How many products? "))

if count <= 0:
    print("Please enter a positive count.")
else:
    for index in range(count):
        name = input(f"Product {index + 1} name: ").strip()
        price = float(input(f"Product {index + 1} price: "))
        quantity = int(input(f"Product {index + 1} quantity: "))
        products.append((name, price, quantity))

    print(f"{'Product':<16}{'Price':>10}{'Qty':>8}{'Total':>12}")
    print("-" * 46)

    grand_total = 0.0
    for name, price, quantity in products:
        total = price * quantity
        grand_total += total
        print(f"{name:<16}{price:>10.2f}{quantity:>8}{total:>12.2f}")

    print("-" * 46)
    print(f"{'Grand total':<34}{grand_total:>12.2f}")
