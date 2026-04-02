# Module focus: Building objects that start valid and stay valid through guarded updates.
# Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints
# easier to reason about.

# Helper setup for constructors and invariants; this keeps the walkthrough readable.
class Temperature:
    def __init__(self, celsius_value: float) -> None:
        # Prepare sample inputs that exercise the key constructors and invariants path.
        self._celsius = max(-273.15, celsius_value)

    def set_celsius(self, new_value: float) -> bool:
        if new_value < -273.15:
            return False

        self._celsius = new_value
        return True

    @property
    def celsius(self) -> float:
        return self._celsius


# Walk through one fixed scenario so constructors and invariants behavior stays repeatable.
def main() -> None:
    temperature = Temperature(-500.0)
    # Report output values so learners can verify the constructors and invariants outcome.
    print(f"Initial value (clamped): {temperature.celsius:.2f} C")

    updated = temperature.set_celsius(25.0)
    print(f"Set to 25.0 success: {updated}")
    print(f"Current value: {temperature.celsius:.2f} C")

    rejected = temperature.set_celsius(-300.0)
    print(f"Set to -300.0 success: {rejected}")

    print(f"Current value: {temperature.celsius:.2f} C")


if __name__ == "__main__":
    main()
