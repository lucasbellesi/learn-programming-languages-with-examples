# This extra example extends copy-and-move semantics with inventory transfer.
# Example purpose: contrast aliasing, cloning, and ownership-like transfer.


class Inventory:
    def __init__(self, items):
        self._items = list(items)

    def clone(self):
        return Inventory(self._items.copy())

    def transfer(self):
        moved_items = self._items
        self._items = []
        return Inventory(moved_items)

    @property
    def items(self):
        return self._items


original = Inventory(["Notebook", "Pencil"])
alias = original
clone = original.clone()
transferred = original.transfer()

alias.items.append("Marker")
clone.items.append("Eraser")

print(f"original items: {original.items}")
print(f"alias items: {alias.items}")
print(f"clone items: {clone.items}")
print(f"transferred items: {transferred.items}")
