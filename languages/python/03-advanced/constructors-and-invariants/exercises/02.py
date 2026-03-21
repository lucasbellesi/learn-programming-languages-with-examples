class SimpleDate:
    def __init__(self, month: int, day: int) -> None:
        self._month = month
        self._day = day

    def is_valid(self) -> bool:
        if self._month < 1 or self._month > 12:
            return False

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return 1 <= self._day <= days_in_month[self._month - 1]


parts = input("Enter month and day: ").strip().split()
if len(parts) != 2:
    print("Invalid input.")
else:
    try:
        month_value = int(parts[0])
        day_value = int(parts[1])
    except ValueError:
        print("Invalid input.")
    else:
        date = SimpleDate(month_value, day_value)
        print("Valid date" if date.is_valid() else "Invalid date")
