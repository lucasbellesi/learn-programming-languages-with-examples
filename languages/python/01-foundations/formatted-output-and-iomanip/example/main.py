# This example demonstrates formatted output and iomanip concepts.
# Example purpose: show the module flow with clear, beginner-friendly steps.

items = [
    ("Notebook", 2, 3.5),
    ("Pencil", 5, 0.8),
    ("Backpack", 1, 29.99),
]

# Intent: print intermediate or final output for quick behavior verification.
print(f"{'Item':<12}{'Qty':>6}{'Unit':>10}{'Total':>10}")
print("-" * 38)

grand_total = 0.0
# Intent: iterate through data in a clear and deterministic order.
for name, qty, unit_price in items:
    total = qty * unit_price
    grand_total += total
    print(f"{name:<12}{qty:>6}{unit_price:>10.2f}{total:>10.2f}")

print("-" * 38)
print(f"{'Grand total':<28}{grand_total:>10.2f}")
