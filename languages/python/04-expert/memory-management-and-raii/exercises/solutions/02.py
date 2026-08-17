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


def run_nested_scopes(depth: int, level: int = 1) -> None:
    if level > depth:
        print(f"Active at deepest scope: {ScopeGuard.active_count}")
        return
    with ScopeGuard(f"scope-{level}"):
        run_nested_scopes(depth, level + 1)


def main() -> None:
    try:
        depth = int(input())
    except ValueError:
        print("Depth must be positive.")
        return
    if depth <= 0:
        print("Depth must be positive.")
        return

    print(f"Active before scopes: {ScopeGuard.active_count}")
    run_nested_scopes(depth)
    print(f"Active after scopes: {ScopeGuard.active_count}")


if __name__ == "__main__":
    main()
