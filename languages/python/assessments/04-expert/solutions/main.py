from __future__ import annotations

import threading


class Summary:
    def __init__(self) -> None:
        self.total = 0
        self.minimum = float("inf")
        self.maximum = float("-inf")


def main() -> None:
    data = [12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6]

    worker_count = 3
    chunk_size = (len(data) + worker_count - 1) // worker_count

    summary = Summary()
    gate = threading.Lock()
    threads: list[threading.Thread] = []

    def worker(worker_id: int, start: int, stop: int) -> None:
        if start >= stop:
            return

        local_values = data[start:stop]
        local_total = sum(local_values)
        local_min = min(local_values)
        local_max = max(local_values)

        with gate:
            print(f"Worker {worker_id} partial sum: {local_total}")
            summary.total += local_total
            summary.minimum = min(summary.minimum, local_min)
            summary.maximum = max(summary.maximum, local_max)

    for worker_id in range(worker_count):
        begin = worker_id * chunk_size
        end = min(begin + chunk_size, len(data))
        thread = threading.Thread(target=worker, args=(worker_id, begin, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print()
    print("Final summary:")
    print(f"Total: {summary.total}")
    print(f"Minimum: {int(summary.minimum)}")
    print(f"Maximum: {int(summary.maximum)}")


if __name__ == "__main__":
    main()
