// Module focus: Protecting object state with defensive collection copies.
// Why it matters: callers should not be able to mutate internal state through an old reference.

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exercise02 {
    static final class TaskBoard {
        private final List<String> tasks;

        TaskBoard(List<String> tasks) {
            // Copy incoming data so later caller changes do not affect this object.
            this.tasks = new ArrayList<>(tasks);
        }

        List<String> tasksSnapshot() {
            return List.copyOf(tasks);
        }

        int size() {
            return tasks.size();
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Invalid count.");
            return;
        }

        int count = scanner.nextInt();
        if (count < 0) {
            System.out.println("Count must not be negative.");
            return;
        }

        List<String> externalTasks = new ArrayList<>();
        for (int index = 0; index < count; index++) {
            if (!scanner.hasNext()) {
                System.out.println("Missing task.");
                return;
            }
            externalTasks.add(scanner.next());
        }

        TaskBoard board = new TaskBoard(externalTasks);
        externalTasks.add("external-change");

        System.out.println("External size: " + externalTasks.size());
        System.out.println("Board size: " + board.size());
        System.out.println("Snapshot size: " + board.tasksSnapshot().size());
    }
}
