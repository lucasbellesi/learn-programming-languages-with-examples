class Counter:
    def __init__(self) -> None:
        self._value = 0

    def increment(self) -> None:
        self._value += 1

    def decrement(self) -> None:
        self._value -= 1

    def reset(self) -> None:
        self._value = 0

    @property
    def value(self) -> int:
        return self._value


counter = Counter()
print("Commands: inc, dec, reset, stop")

while True:
    command = input("Enter command: ").strip().lower()

    if command == "inc":
        counter.increment()
        print(f"Current value: {counter.value}")
        continue

    if command == "dec":
        counter.decrement()
        print(f"Current value: {counter.value}")
        continue

    if command == "reset":
        counter.reset()
        print(f"Current value: {counter.value}")
        continue

    if command == "stop":
        break

    print("Unknown command.")

print(f"Final value: {counter.value}")
