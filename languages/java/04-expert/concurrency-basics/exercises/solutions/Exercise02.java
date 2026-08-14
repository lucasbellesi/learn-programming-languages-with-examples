// Module focus: Coordinating producer and consumer tasks through a blocking queue.
// Why it matters: a completion marker prevents consumers from waiting forever.

import java.util.Scanner;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.LinkedBlockingQueue;

public class Exercise02 {
    private static final int COMPLETED = -1;

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid item count.");
            return;
        }

        int itemCount = scanner.nextInt();
        if (itemCount < 0) {
            System.out.println("Item count cannot be negative.");
            return;
        }

        BlockingQueue<Integer> queue = new LinkedBlockingQueue<>();
        ExecutorService executor = Executors.newFixedThreadPool(2);

        try {
            Future<?> producer = executor.submit(() -> {
                try {
                    for (int value = 1; value <= itemCount; value++) {
                        queue.put(value);
                        System.out.println("Produced: " + value);
                    }
                    queue.put(COMPLETED);
                } catch (InterruptedException error) {
                    Thread.currentThread().interrupt();
                }
            });

            Future<Integer> consumer = executor.submit(() -> {
                int consumed = 0;
                while (true) {
                    int value = queue.take();
                    if (value == COMPLETED) {
                        return consumed;
                    }
                    consumed++;
                    System.out.println("Consumed: " + value);
                }
            });

            producer.get();
            int consumedCount = consumer.get();
            System.out.println("Produced total: " + itemCount);
            System.out.println("Consumed total: " + consumedCount);
        } finally {
            executor.shutdownNow();
        }
    }
}
