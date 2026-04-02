# This example shows formatting values so output is easier to read and compare.
# In Python, the example favors direct readable steps while keeping validation visible.

# Run one direct scenario at the top level so the printed result is easy to verify.
items = [
    ("Notebook", 2, 3.5),
    ("Pencil", 5, 0.8),
    ("Backpack", 1, 29.99),
]

# Print the observed state here so learners can match the code path to the result.
print(f"{'Item':<12}{'Qty':>6}{'Unit':>10}{'Total':>10}")
print("-" * 38)

grand_total = 0.0
for name, qty, unit_price in items:
    total = qty * unit_price
    grand_total += total
    print(f"{name:<12}{qty:>6}{unit_price:>10.2f}{total:>10.2f}")

print("-" * 38)
print(f"{'Grand total':<28}{grand_total:>10.2f}")
