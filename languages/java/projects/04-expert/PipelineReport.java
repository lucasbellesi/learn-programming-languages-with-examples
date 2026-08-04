import java.util.List;

record PipelineReport(
        int jobCount,
        List<StepSummary> steps,
        long elapsedMicroseconds,
        boolean everyJobCompletedEveryStep) {
    PipelineReport {
        steps = List.copyOf(steps);
    }
}
