type Parcel = {
    trackingId: string;
    weightKg: number;
};

class Dock {
    constructor(
        readonly name: string,
        private parcel: Parcel | null,
    ) {}

    moveTo(target: Dock): void {
        if (this.parcel === null) {
            return;
        }

        target.parcel = this.parcel;
        this.parcel = null;
    }

    describe(): string {
        return this.parcel === null
            ? `${this.name}: empty`
            : `${this.name}: ${this.parcel.trackingId} (${this.parcel.weightKg}kg)`;
    }
}

function main(): void {
    const northDock = new Dock("north", {
        trackingId: "PKG-204",
        weightKg: 12,
    });
    const southDock = new Dock("south", null);

    console.log(northDock.describe());
    console.log(southDock.describe());

    northDock.moveTo(southDock);

    console.log(northDock.describe());
    console.log(southDock.describe());
}

main();

export {};
