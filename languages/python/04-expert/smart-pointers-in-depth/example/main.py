# Module focus: Tracking ownership and lifetime when multiple references can observe the same value.
# Why it matters: practicing smart pointers in depth patterns makes exercises and checkpoints easier
# to reason about.

# This example shows tracking ownership and lifetime when multiple references can observe the same
# value.

from __future__ import annotations

import gc
import weakref


# Helper setup for smart pointers in depth; this keeps the walkthrough readable.
class Report:
    def __init__(self, title: str) -> None:
        # Prepare sample inputs that exercise the key smart pointers in depth path.
        self.title = title
        # Report output values so learners can verify the smart pointers in depth outcome.
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


# Walk through one fixed scenario so smart pointers in depth behavior stays repeatable.
def main() -> None:
    inbox = ReportOwner("Inbox", Report("Quarterly Summary"))
    archive = ReportOwner("Archive", None)

    inbox.describe()
    archive.describe()
    inbox.transfer_to(archive)
    inbox.describe()
    archive.describe()

    preview, session = create_preview_session()
    preview.describe()

    session.release()
    gc.collect()
    preview.describe()


if __name__ == "__main__":
    main()
