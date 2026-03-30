class Note:
    def __init__(self, title: str) -> None:
        self.title = title


class NoteHolder:
    def __init__(self, label: str, item: Note | None) -> None:
        self._label = label
        self._item = item

    def move_to(self, destination: "NoteHolder") -> None:
        if self._item is None:
            print(f"{self._label} is empty.")
            return
        print(f"{self._label} moves {self._item.title} to {destination._label}.")
        destination._item = self._item
        self._item = None

    def print(self) -> None:
        print(f"{self._label}: {'empty' if self._item is None else self._item.title}")


def main() -> None:
    active = NoteHolder("Active", Note("Roadmap"))
    backup = NoteHolder("Backup", Note("Old Notes"))
    empty = NoteHolder("Empty", None)

    active.print()
    backup.print()
    active.move_to(backup)
    active.print()
    backup.print()
    empty.move_to(active)
    empty.print()
    active.print()


if __name__ == "__main__":
    main()
