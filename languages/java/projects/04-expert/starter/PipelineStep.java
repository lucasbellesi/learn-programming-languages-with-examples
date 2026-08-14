import java.util.concurrent.atomic.AtomicInteger;

final class PipelineStep {
    private final String name;
    private final AtomicInteger processedCount = new AtomicInteger();

    PipelineStep(String name) {
        if (name == null || name.isBlank()) {
            throw new IllegalArgumentException("Step name must not be blank.");
        }
        this.name = name;
    }

    void process(Job job) {
        if (job == null) {
            throw new IllegalArgumentException("Job must not be null.");
        }
        processedCount.incrementAndGet();
    }

    StepSummary snapshot() {
        return new StepSummary(name, processedCount.get());
    }
}
