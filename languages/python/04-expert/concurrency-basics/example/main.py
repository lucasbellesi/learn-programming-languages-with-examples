# Module focus: Starting multiple units of work and combining their results safely.
# Why it matters: practicing concurrency basics patterns makes exercises and checkpoints easier to
# reason about.

from __future__ import annotations

import queue
import threading


# Walk through one fixed scenario so concurrency basics behavior stays repeatable.
def main() -> None:
    # Prepare sample inputs that exercise the key concurrency basics path.
    worker_count = 4
    increments_per_worker = 10_000
    counter = 0
    counter_lock = threading.Lock()

    def worker() -> None:
        nonlocal counter
        for _ in range(increments_per_worker):
            # The lock makes the read-modify-write update behave as one critical section.
            with counter_lock:
                counter += 1

    # Start all workers before joining so the counter is genuinely shared across threads.
    threads = [threading.Thread(target=worker) for _ in range(worker_count)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    # Report output values so learners can verify the concurrency basics outcome.
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
        # A sentinel tells the consumer that no more work is coming.
        jobs.put(None)

    def consumer() -> None:
        nonlocal consumed_total
        while True:
            value = jobs.get()
            if value is None:
                break
            # Keep aggregation behind a lock even though this example has one consumer.
            with total_lock:
                consumed_total += value
            print(f"Consumed {value}")

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()

    print(f"Consumed total: {consumed_total}")


if __name__ == "__main__":
    main()
