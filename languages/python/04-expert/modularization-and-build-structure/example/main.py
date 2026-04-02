# This example shows splitting responsibilities so entrypoints and helpers stay focused.
# In Python, the example favors direct readable steps while keeping validation visible.

from formatting import render_summary
from pricing import build_summary


# Run one deterministic scenario so the console output makes splitting responsibilities so
# entrypoints and helpers stay focused easy to verify.
def main() -> None:
    # Build the sample state first, then let the later output confirm the behavior step by step.
    items = [
        {"name": "Notebook", "quantity": 2, "unit_price": 3.50},
        {"name": "Pencil", "quantity": 5, "unit_price": 0.80},
        {"name": "Backpack", "quantity": 1, "unit_price": 29.99},
    ]

    summary = build_summary(items, 10.0, 7.5)

    print(render_summary(summary))


if __name__ == "__main__":
    main()
