// This example shows rejecting invalid input before the main workflow continues.
// In TypeScript, the example pairs Node runtime behavior with type annotations where they clarify the flow.

type ValidationResult =
    | { ok: true; value: number }
    | { ok: false; error: string };

function parseIntegerInRange(
    raw: string,
    minimum: number,
    maximum: number,
): ValidationResult {
    const value = Number.parseInt(raw, 10);
    if (!Number.isInteger(value)) {
        return { ok: false, error: "not an integer" };
    }
    if (value < minimum || value > maximum) {
        return { ok: false, error: `outside ${minimum}..${maximum}` };
    }
    return { ok: true, value };
}

const attempts = ["hello", "105", "42"];
for (const attempt of attempts) {
    const result = parseIntegerInRange(attempt, 1, 100);
    if (!result.ok) {
        console.log(
            `Rejected ${JSON.stringify(attempt)} because it is ${result.error}.`,
        );
        continue;
    }

    console.log(`Accepted value: ${result.value}`);
    console.log(`Square: ${result.value * result.value}`);
    break;
}

export {};
