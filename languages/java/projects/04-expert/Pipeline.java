import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;

final class Pipeline implements AutoCloseable {
    private final List<PipelineStep> steps;
    private final ExecutorService executor;
    private final AtomicBoolean started = new AtomicBoolean();

    Pipeline(List<PipelineStep> steps, int workerCount) {
        if (steps == null || steps.isEmpty()) {
            throw new IllegalArgumentException("At least one pipeline step is required.");
        }
        if (workerCount <= 0) {
            throw new IllegalArgumentException("Worker count must be positive.");
        }
        this.steps = List.copyOf(steps);
        this.executor = Executors.newFixedThreadPool(workerCount);
    }

    PipelineReport run(List<Job> jobs) throws InterruptedException, ExecutionException {
        if (!started.compareAndSet(false, true)) {
            throw new IllegalStateException("A pipeline instance can run only once.");
        }
        List<Job> workload = List.copyOf(jobs);
        List<Callable<JobResult>> tasks = new ArrayList<>();
        for (Job job : workload) {
            tasks.add(() -> process(job));
        }

        long started = System.nanoTime();
        List<JobResult> results = new ArrayList<>();
        for (Future<JobResult> future : executor.invokeAll(tasks)) {
            results.add(future.get());
        }
        long elapsedNanos = System.nanoTime() - started;

        List<StepSummary> summaries = steps.stream().map(PipelineStep::snapshot).toList();
        List<String> expectedStepOrder = summaries.stream().map(StepSummary::name).toList();
        boolean complete = results.stream()
                .allMatch(result -> result.completedSteps().equals(expectedStepOrder));
        long elapsedMicroseconds = Math.max(1L, (elapsedNanos + 999L) / 1_000L);
        return new PipelineReport(workload.size(), summaries, elapsedMicroseconds, complete);
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
                    throw new IllegalStateException("Pipeline workers did not terminate.");
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

    private JobResult process(Job job) {
        List<String> completedSteps = new ArrayList<>();
        for (PipelineStep step : steps) {
            step.process(job);
            completedSteps.add(step.snapshot().name());
        }
        return new JobResult(job.id(), completedSteps);
    }
}
