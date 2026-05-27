import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    interface Reportable {
        String reportLine();
    }

    record EnrollmentRequest(String id, String name) {
        EnrollmentRequest {
            if (id == null || id.isBlank()) {
                throw new IllegalArgumentException("id must not be blank");
            }
            if (name == null || name.isBlank()) {
                throw new IllegalArgumentException("name must not be blank");
            }
        }
    }

    static final class EnrollmentBatch {
        private final List<EnrollmentRequest> requests;

        EnrollmentBatch(List<EnrollmentRequest> requests) {
            this.requests = new ArrayList<>(requests);
        }

        List<EnrollmentRequest> snapshot() {
            return List.copyOf(requests);
        }

        int size() {
            return requests.size();
        }
    }

    static final class Course implements Reportable {
        private final String title;
        private final int capacity;
        private final List<EnrollmentRequest> roster = new ArrayList<>();

        Course(String title, int capacity) {
            if (title == null || title.isBlank()) {
                throw new IllegalArgumentException("title must not be blank");
            }
            if (capacity < 0) {
                throw new IllegalArgumentException("capacity must not be negative");
            }
            this.title = title;
            this.capacity = capacity;
        }

        boolean enroll(EnrollmentRequest request) {
            if (hasStudent(request.id()) || roster.size() >= capacity) {
                return false;
            }
            roster.add(request);
            return true;
        }

        List<EnrollmentRequest> rosterSnapshot() {
            return List.copyOf(roster);
        }

        @Override
        public String reportLine() {
            return "Course: " + title + " | " + roster.size() + "/" + capacity + " enrolled";
        }

        private boolean hasStudent(String id) {
            for (EnrollmentRequest request : roster) {
                if (request.id().equals(id)) {
                    return true;
                }
            }
            return false;
        }
    }

    static <T extends Reportable> void printReports(String title, List<T> items) {
        System.out.println(title);
        for (T item : items) {
            System.out.println(item.reportLine());
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid capacity.");
            return;
        }
        int capacity = scanner.nextInt();
        if (capacity < 0) {
            System.out.println("Capacity must not be negative.");
            return;
        }

        if (!scanner.hasNextInt()) {
            System.out.println("Invalid attempt count.");
            return;
        }
        int attemptCount = scanner.nextInt();
        if (attemptCount < 0) {
            System.out.println("Attempt count must not be negative.");
            return;
        }

        List<EnrollmentRequest> externalRequests = new ArrayList<>();
        for (int index = 0; index < attemptCount; index++) {
            if (!scanner.hasNext()) {
                System.out.println("Missing student id.");
                return;
            }
            String id = scanner.next();

            if (!scanner.hasNext()) {
                System.out.println("Missing student name.");
                return;
            }
            String name = scanner.next();
            externalRequests.add(new EnrollmentRequest(id, name));
        }

        EnrollmentBatch batch = new EnrollmentBatch(externalRequests);
        externalRequests.clear();

        Course course = new Course("JavaAdvanced", capacity);
        int accepted = 0;
        int rejected = 0;

        for (EnrollmentRequest request : batch.snapshot()) {
            if (course.enroll(request)) {
                accepted++;
            } else {
                rejected++;
            }
        }

        printReports("Advanced Assessment Report", List.of(course));
        System.out.println("Accepted: " + accepted);
        System.out.println("Rejected: " + rejected);
        System.out.println("External attempts after clear: " + externalRequests.size());
        System.out.println("Batch requests after external clear: " + batch.size());
        System.out.println("Roster snapshot: " + course.rosterSnapshot().size());
    }
}
