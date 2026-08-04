import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;

public class Main {
    record DataSet(List<Integer> values) {
        DataSet {
            if (values == null || values.isEmpty()) {
                throw new IllegalArgumentException("Data set must not be empty.");
            }
            values = List.copyOf(values);
        }
    }

    record WorkerResult(int workerId, long total, int minimum, int maximum) {
    }

    static final class Summary {
        private long total;
        private int minimum = Integer.MAX_VALUE;
        private int maximum = Integer.MIN_VALUE;

        synchronized void merge(WorkerResult result) {
            total += result.total();
            minimum = Math.min(minimum, result.minimum());
            maximum = Math.max(maximum, result.maximum());
        }

        synchronized long total() {
            return total;
        }

        synchronized int minimum() {
            return minimum;
        }

        synchronized int maximum() {
            return maximum;
        }
    }

    static final class WorkerPool implements AutoCloseable {
        private final ExecutorService executor;

        WorkerPool(int workerCount) {
            executor = Executors.newFixedThreadPool(workerCount);
        }

        List<WorkerResult> invokeAll(List<Callable<WorkerResult>> tasks)
                throws InterruptedException, ExecutionException {
            List<WorkerResult> results = new ArrayList<>();
            for (Future<WorkerResult> future : executor.invokeAll(tasks)) {
                results.add(future.get());
            }
            return List.copyOf(results);
        }

        boolean isTerminated() {
            return executor.isTerminated();
        }

        @Override
        public void close() {
            boolean interrupted = false;
            long deadline = System.nanoTime() + TimeUnit.SECONDS.toNanos(10);
            executor.shutdown();
            try {
                while (!executor.isTerminated()) {
                    long remainingNanos = deadline - System.nanoTime();
                    if (remainingNanos <= 0) {
                        executor.shutdownNow();
                        throw new IllegalStateException("Workers did not terminate.");
                    }
                    try {
                        long waitNanos = Math.min(remainingNanos, TimeUnit.SECONDS.toNanos(5));
                        if (!executor.awaitTermination(waitNanos, TimeUnit.NANOSECONDS)) {
                            executor.shutdownNow();
                        }
                    } catch (InterruptedException error) {
                        interrupted = true;
                        executor.shutdownNow();
                    }
                }
            } finally {
                if (interrupted) {
                    Thread.currentThread().interrupt();
                }
            }
        }
    }

    public static void main(String[] args) throws Exception {
        DataSet data = new DataSet(List.of(12, 7, 25, 4, 31, 19, 2, 45, 18, 9, 27, 6));
        int workerCount = 3;
        int chunkSize = (data.values().size() + workerCount - 1) / workerCount;
        Summary summary = new Summary();

        List<Callable<WorkerResult>> tasks = new ArrayList<>();
        for (int workerId = 0; workerId < workerCount; workerId++) {
            int capturedWorkerId = workerId;
            int begin = capturedWorkerId * chunkSize;
            int end = Math.min(begin + chunkSize, data.values().size());
            tasks.add(() -> {
                WorkerResult result = summarizeRange(data, capturedWorkerId, begin, end);
                summary.merge(result);
                return result;
            });
        }

        WorkerPool pool = new WorkerPool(workerCount);
        List<WorkerResult> results;
        try (pool) {
            results = pool.invokeAll(tasks);
        }

        for (WorkerResult result : results) {
            System.out.printf("Worker %d partial sum: %d%n", result.workerId(), result.total());
        }
        System.out.println();
        System.out.println("Final summary:");
        System.out.println("Total: " + summary.total());
        System.out.println("Minimum: " + summary.minimum());
        System.out.println("Maximum: " + summary.maximum());
        System.out.println("Executor terminated: " + pool.isTerminated());
    }

    private static WorkerResult summarizeRange(DataSet data, int workerId, int begin, int end) {
        if (begin >= end) {
            throw new IllegalArgumentException("Every worker must receive at least one value.");
        }

        long total = 0;
        int minimum = data.values().get(begin);
        int maximum = minimum;
        for (int index = begin; index < end; index++) {
            int value = data.values().get(index);
            total += value;
            minimum = Math.min(minimum, value);
            maximum = Math.max(maximum, value);
        }
        return new WorkerResult(workerId, total, minimum, maximum);
    }
}
