// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: practicing input validation patterns makes exercises and checkpoints easier to reason about.

type ValidationResult =
    | { ok: true; value: number }
    | { ok: false; error: string };

function parseIntegerInRange(
    raw: string,
    minimum: number,
    maximum: number,
): ValidationResult {
    // Convert first, then validate the parsed value before business logic uses it.
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
    // Each attempt follows the same parse -> validate -> act shape.
    const result = parseIntegerInRange(attempt, 1, 100);
    if (!result.ok) {
        // Report output values so learners can verify the input validation result.
        console.log(
            `Rejected ${JSON.stringify(attempt)} because it is ${result.error}.`,
        );
        continue;
    }

    // Only validated values reach the main calculation.
    console.log(`Accepted value: ${result.value}`);
    console.log(`Square: ${result.value * result.value}`);
    break;
}

export {};
