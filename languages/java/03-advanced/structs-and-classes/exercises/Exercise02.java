import java.util.Scanner;

public class Exercise02 {
    static class Counter {
        private int value;

        void increment() {
            value++;
        }

        void decrement() {
            value--;
        }

        void reset() {
            value = 0;
        }

        int value() {
            return value;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Counter counter = new Counter();

        while (scanner.hasNext()) {
            String command = scanner.next().trim().toLowerCase();
            if (command.equals("stop")) {
                break;
            }

            switch (command) {
                case "inc" -> counter.increment();
                case "dec" -> counter.decrement();
                case "reset" -> counter.reset();
                default -> {
                    System.out.println("Unknown command: " + command);
                    continue;
                }
            }

            System.out.println("Value: " + counter.value());
        }

        System.out.println("Final value: " + counter.value());
    }
}
