import * as fs from "node:fs";

class BankAccount {
    constructor(
        readonly owner: string,
        readonly balance: number,
    ) {
        if (!owner.trim()) {
            throw new Error("Owner name is required.");
        }
        if (balance < 0) {
            throw new Error("Balance must be non-negative.");
        }
    }
}

function main(): void {
    const tokens = fs
        .readFileSync(0, "utf8")
        .trim()
        .split(/\s+/)
        .filter((token) => token.length > 0);

    const owner = tokens[0] ?? "";
    const openingBalance = Number.parseFloat(tokens[1] ?? "");

    try {
        const account = new BankAccount(owner, openingBalance);
        console.log(`${account.owner}: ${account.balance.toFixed(2)}`);
    } catch (error) {
        console.log((error as Error).message);
    }
}

main();
