# This extra example extends input validation with a menu choice validator.
# Example purpose: keep prompting until the user enters a valid option and quantity.


def read_menu_choice():
    while True:
        raw = input("Choose [1] Add, [2] Remove, [3] Exit: ").strip()
        if raw in {"1", "2", "3"}:
            return raw
        print("Option must be 1, 2, or 3.")


def read_quantity():
    while True:
        raw = input("Enter quantity (1-9): ").strip()
        try:
            quantity = int(raw)
        except ValueError:
            print("Quantity must be an integer.")
            continue

        if 1 <= quantity <= 9:
            return quantity

        print("Quantity must be between 1 and 9.")


choice = read_menu_choice()
if choice == "3":
    print("Nothing to process.")
else:
    quantity = read_quantity()
    action = "added" if choice == "1" else "removed"
    print(f"{quantity} item(s) {action}.")
