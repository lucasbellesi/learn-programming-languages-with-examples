from __future__ import annotations

import threading


def parse_values(raw: str) -> list[int] | None:
    try:
        return [int(piece) for piece in raw.split()]
    except ValueError:
        return None


def main() -> None:
    raw_values = input("Values: ")
    values = parse_values(raw_values)
    if not values:
        print("No valid values provided.")
        return

    try:
        requested_workers = int(input("Worker count: "))
    except ValueError:
        print("Invalid worker count.")
        return

    if requested_workers <= 0:
        print("Worker count must be positive.")
        return

    worker_count = min(requested_workers, len(values))
    chunk_size = (len(values) + worker_count - 1) // worker_count
    partials = [0] * worker_count
    threads: list[threading.Thread] = []

    def make_worker(index: int, start: int, end: int) -> threading.Thread:
        def worker() -> None:
            partials[index] = sum(values[start:end])

        return threading.Thread(target=worker)

    for worker_index in range(worker_count):
        start = worker_index * chunk_size
        end = min(start + chunk_size, len(values))
        thread = make_worker(worker_index, start, end)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = 0
    for worker_index, partial in enumerate(partials, start=1):
        print(f"Worker {worker_index} partial: {partial}")
        total += partial

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
