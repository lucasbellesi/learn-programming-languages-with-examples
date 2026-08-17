from __future__ import annotations

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
    scenario = input()
    cache = WeakCache()
    if scenario == "missing":
        cache.print_lookup("entry")
        return

    value = CachedValue("payload")
    cache.store("entry", value)
    if scenario == "expired":
        del value
    cache.print_lookup("entry")


if __name__ == "__main__":
    main()
