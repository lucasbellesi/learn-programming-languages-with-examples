// Module focus: Proving nested resources close automatically in reverse order.
// Why it matters: scope guards make cleanup reliable when several resources are active.

import java.util.Scanner;

public class Exercise02 {
    static final class ScopeGuard implements AutoCloseable {
        private static int activeGuards = 0;

        private final String name;
        private boolean closed;

        ScopeGuard(String name) {
            this.name = name;
            activeGuards++;
            System.out.printf("enter %s active=%d%n", name, activeGuards);
        }

        static int activeGuards() {
            return activeGuards;
        }

        @Override
        public void close() {
            if (closed) {
                return;
            }
            closed = true;
            activeGuards--;
            System.out.printf("close %s active=%d%n", name, activeGuards);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNextInt()) {
            System.out.println("Depth must be positive.");
            return;
        }
        int depth = scanner.nextInt();
        if (depth <= 0) {
            System.out.println("Depth must be positive.");
            return;
        }

        runNestedScopes(depth, 1);
        System.out.println("final active=" + ScopeGuard.activeGuards());
    }

    static void runNestedScopes(int depth, int level) {
        if (level > depth) {
            System.out.println("inside active=" + ScopeGuard.activeGuards());
            return;
        }

        try (ScopeGuard guard = new ScopeGuard("scope-" + level)) {
            runNestedScopes(depth, level + 1);
        }
    }
}
