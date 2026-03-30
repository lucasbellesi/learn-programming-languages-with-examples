from __future__ import annotations

import gc
import weakref


class CachedValue:
    def __init__(self, text: str) -> None:
        self.text = text


class WeakCache:
    def __init__(self) -> None:
        self._entries: dict[str, weakref.ReferenceType[CachedValue]] = {}

    def store(self, key: str, value: CachedValue) -> None:
        self._entries[key] = weakref.ref(value)

    def print_lookup(self, key: str) -> None:
        reference = self._entries.get(key)
        if reference is None:
            print(f"{key}: missing")
            return

        value = reference()
        if value is None:
            print(f"{key}: expired")
            return

        print(f"{key}: alive -> {value.text}")


def main() -> None:
    cache = WeakCache()
    stable = CachedValue("Still referenced")
    cache.store("stable", stable)

    temporary = CachedValue("Short lived")
    cache.store("temp", temporary)
    cache.print_lookup("stable")
    cache.print_lookup("temp")

    del temporary
    gc.collect()

    cache.print_lookup("stable")
    cache.print_lookup("temp")
    cache.print_lookup("missing")


if __name__ == "__main__":
    main()
