# Example purpose: show threads, locks, and queues in one small runnable flow.

from __future__ import annotations

import queue
import threading


def main() -> None:
    # Program flow: first protect a shared counter, then coordinate producer-consumer work.
    worker_count = 4
    increments_per_worker = 10_000
    counter = 0
    counter_lock = threading.Lock()

    def worker() -> None:
        nonlocal counter
        for _ in range(increments_per_worker):
            with counter_lock:
                counter += 1

    threads = [threading.Thread(target=worker) for _ in range(worker_count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"Expected counter: {worker_count * increments_per_worker}")
    print(f"Actual counter: {counter}")

    print("Producer-consumer demo:")
    jobs: queue.Queue[int | None] = queue.Queue()
    consumed_total = 0
    total_lock = threading.Lock()

    def producer() -> None:
        for value in (10, 20, 30, 40):
            print(f"Produced {value}")
            jobs.put(value)
        jobs.put(None)

    def consumer() -> None:
        nonlocal consumed_total
        while True:
            value = jobs.get()
            if value is None:
                break
            with total_lock:
                consumed_total += value
            print(f"Consumed {value}")

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()

    # Intent: final output verifies the total collected by the consumer thread.
    print(f"Consumed total: {consumed_total}")


if __name__ == "__main__":
    main()
