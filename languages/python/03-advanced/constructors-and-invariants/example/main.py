# Example purpose: show the module flow with clear, beginner-friendly steps.


class Temperature:
    def __init__(self, celsius_value: float) -> None:
        # Intent: enforce the invariant at construction time.
        self._celsius = max(-273.15, celsius_value)

    def set_celsius(self, new_value: float) -> bool:
        if new_value < -273.15:
            return False

        self._celsius = new_value
        return True

    @property
    def celsius(self) -> float:
        return self._celsius


def main() -> None:
    # Program flow: construct with invalid input, then apply valid and invalid updates.
    temperature = Temperature(-500.0)
    print(f"Initial value (clamped): {temperature.celsius:.2f} C")

    updated = temperature.set_celsius(25.0)
    print(f"Set to 25.0 success: {updated}")
    print(f"Current value: {temperature.celsius:.2f} C")

    rejected = temperature.set_celsius(-300.0)
    print(f"Set to -300.0 success: {rejected}")

    # Intent: final state confirms that invariant was preserved.
    print(f"Current value: {temperature.celsius:.2f} C")


if __name__ == "__main__":
    main()
