class Course:
    def __init__(self, title: str, capacity: int) -> None:
        self._title = title
        self._capacity = max(0, capacity)
        self._enrolled = 0

    def enroll(self) -> bool:
        if self._enrolled >= self._capacity:
            return False
        self._enrolled += 1
        return True

    def drop(self) -> bool:
        if self._enrolled <= 0:
            return False
        self._enrolled -= 1
        return True

    def print_status(self) -> None:
        print(f"Course: {self._title} | {self._enrolled}/{self._capacity} enrolled")


def main() -> None:
    python_basics = Course("PythonBasics", 2)
    algorithms = Course("Algorithms", 3)

    python_basics.enroll()
    python_basics.enroll()
    python_basics.enroll()

    algorithms.enroll()

    python_basics.print_status()
    algorithms.print_status()


if __name__ == "__main__":
    main()
