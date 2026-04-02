# This helper example focuses on keeping presentation rules separate from calculations and program
# startup.

from __future__ import annotations


# Keep this helper separate so the main example can focus on the larger idea without extra noise.
def render_summary(summary: dict[str, float]) -> str:
    return (
        f"Subtotal: {summary['subtotal']:.2f}\n"
        f"Discount: {summary['discount_value']:.2f}\n"
        f"Tax: {summary['tax_value']:.2f}\n"
        f"Total: {summary['total']:.2f}"
    )
