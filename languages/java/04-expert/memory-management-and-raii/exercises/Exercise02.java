// Module focus: Proving nested resources close automatically in reverse order.
// Why it matters: scope guards make cleanup reliable when several resources are active.

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
        try (ScopeGuard outer = new ScopeGuard("outer")) {
            try (ScopeGuard inner = new ScopeGuard("inner")) {
                System.out.println("inside active=" + ScopeGuard.activeGuards());
            }
        }

        System.out.println("final active=" + ScopeGuard.activeGuards());
    }
}
