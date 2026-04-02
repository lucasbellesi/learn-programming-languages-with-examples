# Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
# Why it matters: practicing modularization and build structure patterns makes exercises and
# checkpoints easier to reason about.

from formatting import render_summary
from pricing import build_summary


# Walk through one fixed scenario so modularization and build structure behavior stays repeatable.
def main() -> None:
    # Prepare sample inputs that exercise the key modularization and build structure path.
    items = [
        {"name": "Notebook", "quantity": 2, "unit_price": 3.50},
        {"name": "Pencil", "quantity": 5, "unit_price": 0.80},
        {"name": "Backpack", "quantity": 1, "unit_price": 29.99},
    ]

    summary = build_summary(items, 10.0, 7.5)

    # Report output values so learners can verify the modularization and build structure outcome.
    print(render_summary(summary))


if __name__ == "__main__":
    main()
