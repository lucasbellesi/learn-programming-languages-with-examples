import * as fs from "node:fs";

class BankAccount {
    constructor(
        readonly owner: string,
        readonly balance: number,
    ) {
        if (!owner.trim()) {
            throw new Error("Owner name is required.");
        }
        if (Number.isNaN(balance)) {
            throw new Error("Opening balance must be numeric.");
        }
        if (balance < 0) {
            throw new Error("Balance must be non-negative.");
        }
    }
}

function main(): void {
    const lines = fs.readFileSync(0, "utf8").replace(/\r/g, "").split("\n");
    const owner = (lines[0] ?? "").trim();
    const openingBalance = Number.parseFloat((lines[1] ?? "").trim());

    try {
        const account = new BankAccount(owner, openingBalance);
        console.log(`${account.owner}: ${account.balance.toFixed(2)}`);
    } catch (error) {
        console.log((error as Error).message);
    }
}

main();
