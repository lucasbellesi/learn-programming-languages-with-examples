from __future__ import annotations

import queue
import threading


def main() -> None:
    try:
        count = int(input("Items to produce: "))
    except ValueError:
        print("Invalid item count.")
        return

    if count < 0:
        print("Item count cannot be negative.")
        return

    items: queue.Queue[int | None] = queue.Queue()
    consumed = 0

    def producer() -> None:
        for value in range(1, count + 1):
            print(f"Produced {value}")
            items.put(value)
        items.put(None)

    def consumer() -> None:
        nonlocal consumed
        while True:
            value = items.get()
            if value is None:
                break
            consumed += 1
            print(f"Consumed {value}")

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    producer_thread.start()
    consumer_thread.start()
    producer_thread.join()
    consumer_thread.join()

    print(f"Produced total: {count}")
    print(f"Consumed total: {consumed}")


if __name__ == "__main__":
    main()
