record Job(String id) {
    Job {
        if (id == null || id.isBlank()) {
            throw new IllegalArgumentException("Job id must not be blank.");
        }
    }
}
