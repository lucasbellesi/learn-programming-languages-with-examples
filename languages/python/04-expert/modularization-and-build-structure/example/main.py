# Example purpose: show a modular structure by separating pricing, formatting, and orchestration.

from formatting import render_summary
from pricing import build_summary


def main() -> None:
    # Program flow: define input data, delegate calculations, then format a report.
    items = [
        {"name": "Notebook", "quantity": 2, "unit_price": 3.50},
        {"name": "Pencil", "quantity": 5, "unit_price": 0.80},
        {"name": "Backpack", "quantity": 1, "unit_price": 29.99},
    ]

    summary = build_summary(items, 10.0, 7.5)

    # Intent: keep console output in the entrypoint while reusable logic stays in helpers.
    print(render_summary(summary))


if __name__ == "__main__":
    main()
