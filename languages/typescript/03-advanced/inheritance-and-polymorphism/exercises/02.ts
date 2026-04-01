import * as fs from "node:fs";

interface Renderer {
    render(label: string): string;
}

class UppercaseRenderer implements Renderer {
    render(label: string): string {
        return label.toUpperCase();
    }
}

class BracketRenderer implements Renderer {
    render(label: string): string {
        return `[${label}]`;
    }
}

function main(): void {
    const label = fs.readFileSync(0, "utf8").trim();
    if (!label) {
        console.log("Label is required.");
        return;
    }

    const renderers: Renderer[] = [
        new UppercaseRenderer(),
        new BracketRenderer(),
    ];
    for (const renderer of renderers) {
        console.log(renderer.render(label));
    }
}

main();
