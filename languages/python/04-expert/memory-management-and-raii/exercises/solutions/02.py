class ScopeGuard:
    active_count = 0

    def __init__(self, label: str) -> None:
        self._label = label
        self._closed = False

    def __enter__(self) -> "ScopeGuard":
        ScopeGuard.active_count += 1
        print(f"enter {self._label} (active={ScopeGuard.active_count})")
        return self

    def __exit__(self, exc_type, exc, exc_tb) -> None:
        self.close()

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        ScopeGuard.active_count -= 1
        print(f"exit {self._label} (active={ScopeGuard.active_count})")


def main() -> None:
    print(f"Active before scopes: {ScopeGuard.active_count}")
    with ScopeGuard("outer"):
        print(f"Active inside outer: {ScopeGuard.active_count}")
        with ScopeGuard("inner"):
            print(f"Active inside inner: {ScopeGuard.active_count}")
        print(f"Active after inner: {ScopeGuard.active_count}")
    print(f"Active after scopes: {ScopeGuard.active_count}")


if __name__ == "__main__":
    main()
