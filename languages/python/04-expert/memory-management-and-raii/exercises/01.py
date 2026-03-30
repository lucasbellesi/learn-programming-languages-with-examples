class OwnedBuffer:
    def __init__(self, size: int) -> None:
        self._values = [0] * size
        self._closed = False

    def __enter__(self) -> "OwnedBuffer":
        return self

    def __exit__(self, exc_type, exc, exc_tb) -> None:
        self.close()

    def set_at(self, index: int, value: int) -> None:
        self._ensure_open()
        self._values[index] = value

    def get_at(self, index: int) -> int:
        self._ensure_open()
        return self._values[index]

    def total(self) -> int:
        self._ensure_open()
        return sum(self._values)

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._values.clear()

    def _ensure_open(self) -> None:
        if self._closed:
            raise RuntimeError("buffer already closed")


def main() -> None:
    try:
        count = int(input("Count: "))
    except ValueError:
        print("Invalid count.")
        return

    if count <= 0:
        print("Count must be positive.")
        return

    with OwnedBuffer(count) as buffer:
        for index in range(count):
            try:
                value = int(input(f"Value {index + 1}: "))
            except ValueError:
                print("Invalid integer input.")
                return
            buffer.set_at(index, value)

        print(f"Sum: {buffer.total()}")
        reversed_values = [str(buffer.get_at(index)) for index in range(count - 1, -1, -1)]
        print("Reversed: " + " ".join(reversed_values))


if __name__ == "__main__":
    main()
