from __future__ import annotations


def render_summary(summary: dict[str, float]) -> str:
    return (
        f"Subtotal: {summary['subtotal']:.2f}\n"
        f"Discount: {summary['discount_value']:.2f}\n"
        f"Tax: {summary['tax_value']:.2f}\n"
        f"Total: {summary['total']:.2f}"
    )
