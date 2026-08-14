// Module focus: Splitting a sum across workers without sharing partial-result mutations.
// Why it matters: futures keep worker results ordered and make aggregation explicit.

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Exercise01 {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid value count.");
            return;
        }

        int valueCount = scanner.nextInt();
        if (valueCount <= 0) {
            System.out.println("Value count must be positive.");
            return;
        }

        List<Integer> values = new ArrayList<>();
        for (int index = 0; index < valueCount; index++) {
            if (!scanner.hasNextInt()) {
                System.out.println("Invalid value.");
                return;
            }
            values.add(scanner.nextInt());
        }

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid worker count.");
            return;
        }
        int requestedWorkers = scanner.nextInt();
        if (requestedWorkers <= 0) {
            System.out.println("Worker count must be positive.");
            return;
        }

        int workerCount = Math.min(requestedWorkers, valueCount);
        int chunkSize = (valueCount + workerCount - 1) / workerCount;
        ExecutorService executor = Executors.newFixedThreadPool(workerCount);
        List<Callable<Long>> tasks = new ArrayList<>();

        for (int workerIndex = 0; workerIndex < workerCount; workerIndex++) {
            int start = workerIndex * chunkSize;
            int end = Math.min(start + chunkSize, valueCount);
            tasks.add(() -> {
                long partial = 0;
                for (int index = start; index < end; index++) {
                    partial += values.get(index);
                }
                return partial;
            });
        }

        long total = 0;
        try {
            List<Future<Long>> results = executor.invokeAll(tasks);
            for (int index = 0; index < results.size(); index++) {
                long partial = results.get(index).get();
                total += partial;
                System.out.printf("Worker %d partial: %d%n", index + 1, partial);
            }
        } finally {
            executor.shutdownNow();
        }

        System.out.println("Workers used: " + workerCount);
        System.out.println("Final total: " + total);
    }
}
