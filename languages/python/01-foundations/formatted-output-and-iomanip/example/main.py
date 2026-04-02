# Module focus: Formatting values so output is easier to read and compare.
# Why it matters: practicing formatted output and iomanip patterns makes exercises and checkpoints
# easier to reason about.

# Walk through one fixed scenario so formatted output and iomanip behavior stays repeatable.
items = [
    ("Notebook", 2, 3.5),
    ("Pencil", 5, 0.8),
    ("Backpack", 1, 29.99),
]

# Report values so learners can verify the formatted output and iomanip outcome.
print(f"{'Item':<12}{'Qty':>6}{'Unit':>10}{'Total':>10}")
print("-" * 38)

grand_total = 0.0
for name, qty, unit_price in items:
    total = qty * unit_price
    grand_total += total
    print(f"{name:<12}{qty:>6}{unit_price:>10.2f}{total:>10.2f}")

print("-" * 38)
print(f"{'Grand total':<28}{grand_total:>10.2f}")
