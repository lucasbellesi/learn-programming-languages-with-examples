// Module focus: Building objects that start valid and stay valid through guarded updates.
// Why it matters: practicing constructors and invariants patterns makes exercises and checkpoints easier to reason about.

class BankAccount {
    #balance: number;

    constructor(
        readonly owner: string,
        openingBalance: number,
    ) {
        // Reject invalid construction so no BankAccount starts in a broken state.
        if (!owner.trim()) {
            throw new Error("Owner name is required.");
        }
        if (openingBalance < 0) {
            throw new Error("Opening balance must be non-negative.");
        }
        this.#balance = openingBalance;
    }

    deposit(amount: number): void {
        // Guard every state-changing method, not only the constructor.
        if (amount <= 0) {
            throw new Error("Deposit amount must be positive.");
        }
        this.#balance += amount;
    }

    withdraw(amount: number): boolean {
        if (amount <= 0 || amount > this.#balance) {
            return false;
        }
        this.#balance -= amount;
        return true;
    }

    printStatus(): void {
        // Report output values so learners can verify the constructors and invariants result.
        console.log(`${this.owner}: ${this.#balance.toFixed(2)}`);
    }
}

// The valid scenario shows normal updates after the invariant checks pass.
const account = new BankAccount("Ana", 120);
account.deposit(30);
account.withdraw(50);
account.printStatus();

export {};
