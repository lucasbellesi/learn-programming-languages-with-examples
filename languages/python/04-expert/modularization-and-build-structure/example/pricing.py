from __future__ import annotations


def build_summary(
    items: list[dict[str, float]], discount_percent: float, tax_percent: float
) -> dict[str, float]:
    subtotal = sum(item["quantity"] * item["unit_price"] for item in items)
    discount_value = subtotal * (discount_percent / 100.0)
    taxed_base = subtotal - discount_value
    tax_value = taxed_base * (tax_percent / 100.0)
    return {
        "subtotal": subtotal,
        "discount_value": discount_value,
        "tax_value": tax_value,
        "total": taxed_base + tax_value,
    }
