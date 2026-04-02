# This example shows building objects that start valid and stay valid through guarded updates.
# In Python, the example favors direct readable steps while keeping validation visible.

# Define the reusable pieces first so the main flow can focus on one observable scenario.
class Temperature:
    def __init__(self, celsius_value: float) -> None:
        # Build the sample state first, then let the later output confirm the behavior step by step.
        self._celsius = max(-273.15, celsius_value)

    def set_celsius(self, new_value: float) -> bool:
        if new_value < -273.15:
            return False

        self._celsius = new_value
        return True

    @property
    def celsius(self) -> float:
        return self._celsius


# Run one deterministic scenario so the console output makes building objects that start valid and
# stay valid through guarded updates easy to verify.
def main() -> None:
    temperature = Temperature(-500.0)
    print(f"Initial value (clamped): {temperature.celsius:.2f} C")

    updated = temperature.set_celsius(25.0)
    print(f"Set to 25.0 success: {updated}")
    print(f"Current value: {temperature.celsius:.2f} C")

    rejected = temperature.set_celsius(-300.0)
    print(f"Set to -300.0 success: {rejected}")

    print(f"Current value: {temperature.celsius:.2f} C")


if __name__ == "__main__":
    main()
