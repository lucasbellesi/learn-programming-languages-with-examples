import java.util.ArrayList;
import java.util.List;

public class Main {
    interface Reportable {
        String reportLine();
    }

    record Student(String id, String name) {
        Student {
            if (id == null || id.isBlank()) {
                throw new IllegalArgumentException("id must not be blank");
            }
            if (name == null || name.isBlank()) {
                throw new IllegalArgumentException("name must not be blank");
            }
        }
    }

    static final class Course implements Reportable {
        private final String title;
        private final int capacity;
        private final List<Student> enrolled = new ArrayList<>();

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

        boolean enroll(Student student) {
            if (enrolled.size() >= capacity || hasStudent(student.id())) {
                return false;
            }
            enrolled.add(student);
            return true;
        }

        boolean dropById(String studentId) {
            return enrolled.removeIf(student -> student.id().equals(studentId));
        }

        List<Student> rosterSnapshot() {
            return List.copyOf(enrolled);
        }

        @Override
        public String reportLine() {
            return "Course: " + title + " | " + enrolled.size() + "/" + capacity + " enrolled";
        }

        private boolean hasStudent(String studentId) {
            for (Student student : enrolled) {
                if (student.id().equals(studentId)) {
                    return true;
                }
            }
            return false;
        }
    }

    static final class Catalog<T extends Reportable> {
        private final List<T> items;

        Catalog(List<T> items) {
            this.items = new ArrayList<>(items);
        }

        List<T> snapshot() {
            return List.copyOf(items);
        }
    }

    static <T extends Reportable> void printReport(String title, List<T> items) {
        System.out.println(title);
        for (T item : items) {
            System.out.println(item.reportLine());
        }
    }

    public static void main(String[] args) {
        Student ana = new Student("S-101", "Ana Smith");
        Student bob = new Student("S-202", "Bob Lee");
        Student carla = new Student("S-303", "Carla Mendez");

        Course javaAdvanced = new Course("JavaAdvanced", 2);
        Course algorithms = new Course("Algorithms", 3);

        javaAdvanced.enroll(ana);
        javaAdvanced.enroll(bob);
        boolean overflowAccepted = javaAdvanced.enroll(carla);

        algorithms.enroll(carla);
        algorithms.dropById("S-404");

        List<Course> externalCourses = new ArrayList<>();
        externalCourses.add(javaAdvanced);
        externalCourses.add(algorithms);
        Catalog<Course> catalog = new Catalog<>(externalCourses);
        externalCourses.clear();

        printReport("Course Enrollment Report", catalog.snapshot());
        System.out.println("Overflow accepted: " + overflowAccepted);
        System.out.println("Catalog courses after external clear: " + catalog.snapshot().size());
        System.out.println("JavaAdvanced roster snapshot: " + javaAdvanced.rosterSnapshot().size());
    }
}
