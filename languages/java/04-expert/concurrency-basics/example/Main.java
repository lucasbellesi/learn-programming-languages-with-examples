// Module focus: Starting multiple units of work and combining their results safely.
// Why it matters: the example makes it possible to coordinate concurrent work without data races
// or lost results before the learner tackles the exercises.

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class Main {
    // Encapsulating the counter keeps synchronization next to the state it protects.
    static final class SafeCounter {
        private int value;

        // The instance monitor allows only one worker to mutate the counter at a time.
        synchronized void increment() {
            value++;
        }

        synchronized int value() {
            return value;
        }
    }

    public static void main(String[] args) throws InterruptedException, ExecutionException {
        final int workerCount = 4;
        final int incrementsPerWorker = 10_000;
        SafeCounter counter = new SafeCounter();
        ExecutorService executor = Executors.newFixedThreadPool(workerCount);

        // Tasks describe units of work without exposing executor implementation details.
        List<Callable<Integer>> tasks = new ArrayList<>();
        for (int workerIndex = 0; workerIndex < workerCount; workerIndex++) {
            // Each task returns its own result while synchronizing the one shared counter.
            tasks.add(() -> {
                for (int step = 0; step < incrementsPerWorker; step++) {
                    counter.increment();
                }
                return incrementsPerWorker;
            });
        }

        List<Integer> completedWork = new ArrayList<>();
        try {
            // invokeAll preserves task order even though worker completion order can vary.
            for (Future<Integer> result : executor.invokeAll(tasks)) {
                completedWork.add(result.get());
            }
        } finally {
            executor.shutdown();
            if (!executor.awaitTermination(5, TimeUnit.SECONDS)) {
                executor.shutdownNow();
            }
        }

        int expected = workerCount * incrementsPerWorker;
        // Report deterministic values after every worker has completed.
        System.out.println("Worker results: " + completedWork);
        System.out.println("Expected counter: " + expected);
        System.out.println("Actual counter: " + counter.value());
        System.out.println("Counter is correct: " + (counter.value() == expected));
        System.out.println("Executor terminated: " + executor.isTerminated());
    }
}
