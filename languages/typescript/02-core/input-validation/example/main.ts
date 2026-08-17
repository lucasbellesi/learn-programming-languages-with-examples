// Module focus: Rejecting invalid input before the main workflow continues.
// Why it matters: the example makes it possible to reject malformed and out-of-domain input
// without corrupting state before the learner tackles the exercises.

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
        // The printed result shows whether the program can design retry and termination behavior
        // that cannot loop accidentally.
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
