class IntBuffer:
    def __init__(self, size: int) -> None:
        safe_size = max(0, size)
        self._values = [0] * safe_size
        print(f"Constructed IntBuffer (size={len(self._values)})")

    @classmethod
    def _from_values(cls, values: list[int]) -> "IntBuffer":
        obj = cls(0)
        obj._values = values
        print(f"Transferred IntBuffer (size={len(values)})")
        return obj

    def clone(self) -> "IntBuffer":
        cloned = IntBuffer(0)
        cloned._values = self._values.copy()
        print("Cloned IntBuffer")
        return cloned

    def transfer(self) -> "IntBuffer":
        moved_values = self._values
        self._values = []
        return IntBuffer._from_values(moved_values)

    @property
    def size(self) -> int:
        return len(self._values)


a = IntBuffer(4)
b = a.clone()
c = b.transfer()

print(f"a size: {a.size}")
print(f"b size: {b.size}")
print(f"c size: {c.size}")
