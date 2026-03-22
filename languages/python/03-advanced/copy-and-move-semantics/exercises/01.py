class IntBuffer:
    def __init__(self, values: list[int]) -> None:
        self._values = values.copy()
        print(f"Constructed IntBuffer (size={len(self._values)})")

    def clone(self) -> "IntBuffer":
        cloned = IntBuffer.__new__(IntBuffer)
        cloned._values = self._values.copy()
        print("Cloned IntBuffer")
        return cloned

    def transfer(self) -> "IntBuffer":
        moved_values = self._values
        self._values = []
        transferred = IntBuffer.__new__(IntBuffer)
        transferred._values = moved_values
        print(f"Transferred IntBuffer (size={len(moved_values)})")
        return transferred

    @property
    def size(self) -> int:
        return len(self._values)


raw_size = input("Buffer size: ").strip()
try:
    size = int(raw_size)
except ValueError:
    print("Invalid size.")
else:
    if size < 0:
        print("Invalid size.")
    else:
        raw_values = input("Buffer values: ").strip().split()
        if len(raw_values) != size:
            print("The amount of values must match the buffer size.")
        else:
            try:
                parsed_values = [int(part) for part in raw_values]
            except ValueError:
                print("Invalid value detected.")
            else:
                a = IntBuffer(parsed_values)
                b = a.clone()
                c = b.transfer()

                print(f"a size: {a.size}")
                print(f"b size: {b.size}")
                print(f"c size: {c.size}")
