import { readFileSync } from "node:fs";

type Parcel = {
    trackingId: string;
    weightKg: number;
};

class Dock {
    constructor(
        readonly name: string,
        private parcel: Parcel | null,
    ) {}

    moveTo(target: Dock): string {
        if (this.parcel === null) {
            return "source empty";
        }
        if (target.parcel !== null) {
            return "destination occupied";
        }

        target.parcel = this.parcel;
        this.parcel = null;
        return "moved";
    }

    describe(): string {
        return this.parcel === null
            ? `${this.name}: empty`
            : `${this.name}: ${this.parcel.trackingId} (${this.parcel.weightKg}kg)`;
    }
}

function main(): void {
    const [sourceLine = "empty", targetLine = "empty"] = readFileSync(0, "utf8")
        .trimEnd()
        .split(/\r?\n/);
    const parseParcel = (line: string): Parcel | null => {
        if (line.trim() === "empty") {
            return null;
        }
        const [trackingId = "unknown", weight = "0"] = line.split("|");
        return { trackingId: trackingId.trim(), weightKg: Number(weight) };
    };
    const northDock = new Dock("north", parseParcel(sourceLine));
    const southDock = new Dock("south", parseParcel(targetLine));

    console.log(northDock.describe());
    console.log(southDock.describe());

    console.log(`Transfer: ${northDock.moveTo(southDock)}`);

    console.log(northDock.describe());
    console.log(southDock.describe());
}

main();

export {};
