subtotal = float(input("Subtotal: "))
discount_percent = float(input("Discount percent: "))
tax_percent = float(input("Tax percent: "))

if subtotal < 0:
    print("Subtotal must be non-negative.")
else:
    discount_value = subtotal * (discount_percent / 100)
    discounted_total = subtotal - discount_value
    tax_value = discounted_total * (tax_percent / 100)
    final_total = discounted_total + tax_value

    print(f"Discount value: {discount_value:.2f}")
    print(f"Tax value: {tax_value:.2f}")
    print(f"Final total: {final_total:.2f}")
