# Module focus: Splitting responsibilities so entrypoints and helpers stay focused.
# Why it matters: the example makes it possible to separate public contracts from
# implementation details before the learner tackles the exercises.

from formatting import render_summary
from pricing import build_summary


# Fixed inputs make the consequence of putting every concern directly into `main.py` visible and
# repeatable.
def main() -> None:
    # These values exercise the normal path before the exercises vary the documented boundaries.
    items = [
        {"name": "Notebook", "quantity": 2, "unit_price": 3.50},
        {"name": "Pencil", "quantity": 5, "unit_price": 0.80},
        {"name": "Backpack", "quantity": 1, "unit_price": 29.99},
    ]

    summary = build_summary(items, 10.0, 7.5)

    # The printed result shows whether the program can organize a multi-file program with an
    # explicit build boundary.
    print(render_summary(summary))


if __name__ == "__main__":
    main()
