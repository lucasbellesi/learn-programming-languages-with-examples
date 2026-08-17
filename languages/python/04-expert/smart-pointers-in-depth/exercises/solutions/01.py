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
        if destination._item is not None:
            print(f"{destination._label} is occupied.")
            return
        print(f"{self._label} moves {self._item.title} to {destination._label}.")
        destination._item = self._item
        self._item = None

    def print(self) -> None:
        print(f"{self._label}: {'empty' if self._item is None else self._item.title}")


def main() -> None:
    source_title = input()
    destination_title = input()
    active = NoteHolder("Source", None if source_title == "empty" else Note(source_title))
    backup = NoteHolder(
        "Destination", None if destination_title == "empty" else Note(destination_title)
    )

    active.print()
    backup.print()
    active.move_to(backup)
    active.print()
    backup.print()


if __name__ == "__main__":
    main()
