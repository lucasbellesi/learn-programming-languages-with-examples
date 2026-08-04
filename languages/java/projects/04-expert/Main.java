import java.util.List;

public class Main {
    public static void main(String[] args) throws Exception {
        List<Job> jobs = List.of(
                new Job("JOB-101"),
                new Job("JOB-202"),
                new Job("JOB-303"));
        List<PipelineStep> steps = List.of(
                new PipelineStep("load"),
                new PipelineStep("transform"));

        Pipeline pipeline = new Pipeline(steps, 3);
        PipelineReport report;
        try (pipeline) {
            report = pipeline.run(jobs);
        }

        System.out.printf(
                "Running %d jobs through %d steps...%n",
                report.jobCount(),
                report.steps().size());
        for (StepSummary step : report.steps()) {
            System.out.printf(
                    "Step %s processed %d jobs%n",
                    step.name(),
                    step.processedCount());
        }
        System.out.println("Every job completed every step: " + report.everyJobCompletedEveryStep());
        System.out.println("Executor terminated: " + pipeline.isTerminated());
        System.out.println("Elapsed (microseconds): " + report.elapsedMicroseconds());
    }
}
