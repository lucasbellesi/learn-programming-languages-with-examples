// This example shows building objects that start valid and stay valid through guarded updates.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

class BankAccount {
    #balance: number;

    constructor(
        readonly owner: string,
        openingBalance: number,
    ) {
        if (!owner.trim()) {
            throw new Error("Owner name is required.");
        }
        if (openingBalance < 0) {
            throw new Error("Opening balance must be non-negative.");
        }
        this.#balance = openingBalance;
    }

    deposit(amount: number): void {
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
        console.log(`${this.owner}: ${this.#balance.toFixed(2)}`);
    }
}

const account = new BankAccount("Ana", 120);
account.deposit(30);
account.withdraw(50);
account.printStatus();

export {};
