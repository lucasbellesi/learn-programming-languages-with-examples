def validate_percent(value: float) -> bool:
    return 0.0 <= value <= 100.0


def build_totals(
    subtotal: float, discount_percent: float, tax_percent: float
) -> tuple[float, float, float] | None:
    if (
        subtotal < 0.0
        or not validate_percent(discount_percent)
        or not validate_percent(tax_percent)
    ):
        return None

    discount_value = subtotal * (discount_percent / 100.0)
    taxed_base = subtotal - discount_value
    tax_value = taxed_base * (tax_percent / 100.0)
    return discount_value, tax_value, taxed_base + tax_value


def main() -> None:
    try:
        subtotal = float(input("Subtotal: "))
        discount_percent = float(input("Discount %: "))
        tax_percent = float(input("Tax %: "))
    except ValueError:
        print("Invalid input.")
        return

    totals = build_totals(subtotal, discount_percent, tax_percent)
    if totals is None:
        print("Values out of range.")
        return

    discount_value, tax_value, total = totals
    print(f"Discount: {discount_value:.2f}")
    print(f"Tax: {tax_value:.2f}")
    print(f"Total: {total:.2f}")


if __name__ == "__main__":
    main()
