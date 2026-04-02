# This helper example focuses on isolating the arithmetic so the learner can verify each pricing
# step.

# This extra example extends operators and expressions with an invoice breakdown.

subtotal = 84.50
discount_percent = 12.0
tax_percent = 21.0
shipping = 7.50

discount_value = subtotal * discount_percent / 100.0
taxable_base = subtotal - discount_value
tax_value = taxable_base * tax_percent / 100.0
final_total = taxable_base + tax_value + shipping

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: -{discount_value:.2f}")
print(f"Taxable base: {taxable_base:.2f}")
print(f"Tax: +{tax_value:.2f}")
print(f"Shipping: +{shipping:.2f}")
print(f"Final total: {final_total:.2f}")
