# Example purpose: adapt smart-pointer ideas to ownership transfer and weak references in Python.

from __future__ import annotations

import gc
import weakref


class Report:
    def __init__(self, title: str) -> None:
        self.title = title
        print(f"Created report: {title}")


class ReportOwner:
    def __init__(self, name: str, report: Report | None) -> None:
        self._name = name
        self._report = report

    def transfer_to(self, destination: "ReportOwner") -> None:
        if self._report is None:
            print(f"{self._name} has nothing to transfer.")
            return
        print(f"{self._name} transfers {self._report.title} to {destination._name}.")
        destination._report = self._report
        self._report = None

    def describe(self) -> None:
        print(f"{self._name}: {'empty' if self._report is None else self._report.title}")


class PreviewPane:
    def __init__(self, report: Report) -> None:
        self._report_ref = weakref.ref(report)

    def describe(self) -> None:
        report = self._report_ref()
        if report is None:
            print("Preview target expired.")
            return
        print(f"Preview can still see: {report.title}")


class PreviewSession:
    def __init__(self, report: Report) -> None:
        self._report = report

    @property
    def current(self) -> Report | None:
        return self._report

    def release(self) -> None:
        self._report = None


def create_preview_session() -> tuple[PreviewPane, PreviewSession]:
    session = PreviewSession(Report("Transient Draft"))
    current = session.current
    assert current is not None
    return PreviewPane(current), session


def main() -> None:
    # Program flow: move one strongly-owned reference, then release a temporary strong owner.
    inbox = ReportOwner("Inbox", Report("Quarterly Summary"))
    archive = ReportOwner("Archive", None)

    inbox.describe()
    archive.describe()
    inbox.transfer_to(archive)
    inbox.describe()
    archive.describe()

    preview, session = create_preview_session()
    preview.describe()

    # Intent: dropping the last strong owner makes the weak observer expire on the next collection.
    session.release()
    gc.collect()
    preview.describe()


if __name__ == "__main__":
    main()
