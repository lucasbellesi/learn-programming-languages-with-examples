import java.util.Locale;
import java.util.Scanner;

public class Exercise01 {
    static class BankAccount {
        private double balance;

        BankAccount(double initialBalance) {
            balance = Math.max(0.0, initialBalance);
        }

        boolean deposit(double amount) {
            if (amount <= 0.0) {
                return false;
            }
            balance += amount;
            return true;
        }

        boolean withdraw(double amount) {
            if (amount <= 0.0 || amount > balance) {
                return false;
            }
            balance -= amount;
            return true;
        }

        double balance() {
            return balance;
        }
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);

        double initialBalance = scanner.nextDouble();
        BankAccount account = new BankAccount(initialBalance);

        double depositAmount = scanner.nextDouble();
        account.deposit(depositAmount);

        double withdrawAmount = scanner.nextDouble();
        if (!account.withdraw(withdrawAmount)) {
            System.out.println("Withdrawal rejected.");
        }

        System.out.printf("Final balance: %.2f%n", account.balance());
    }
}
