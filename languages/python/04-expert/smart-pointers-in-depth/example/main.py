# Example purpose: adapt smart-pointer ideas to ownership transfer and weak references in Python.

from __future__ import annotations

import gc
import weakref


class Report:
    def __init__(self, title: str) -> None:
        self.title = title
        print(f"Created report: {title}")

    def __del__(self) -> None:
        print(f"Finalized report: {self.title}")


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


def make_preview() -> PreviewPane:
    transient = Report("Transient Draft")
    return PreviewPane(transient)


def main() -> None:
    # Program flow: move one strongly-owned reference, then watch a weak observer expire.
    inbox = ReportOwner("Inbox", Report("Quarterly Summary"))
    archive = ReportOwner("Archive", None)

    inbox.describe()
    archive.describe()
    inbox.transfer_to(archive)
    inbox.describe()
    archive.describe()

    preview = make_preview()
    preview.describe()
    gc.collect()

    # Intent: final state confirms that the weak observer did not keep the object alive.
    preview.describe()


if __name__ == "__main__":
    main()
