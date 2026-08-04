import java.util.List;

record JobResult(String jobId, List<String> completedSteps) {
    JobResult {
        completedSteps = List.copyOf(completedSteps);
    }
}
