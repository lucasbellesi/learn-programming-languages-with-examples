type ServiceConfig = {
    name: string;
    retryCount: number;
};

function validateConfig(config: ServiceConfig): string[] {
    const problems: string[] = [];
    if (config.name.trim().length === 0) {
        problems.push("Service name is required.");
    }
    if (config.retryCount < 0) {
        problems.push("Retry count cannot be negative.");
    }
    return problems;
}

function renderConfig(config: ServiceConfig): string {
    return [`Service: ${config.name}`, `Retries: ${config.retryCount}`].join(
        "\n",
    );
}

function main(): void {
    const config: ServiceConfig = {
        name: "notifications",
        retryCount: 3,
    };
    const problems = validateConfig(config);

    if (problems.length > 0) {
        for (const problem of problems) {
            console.log(problem);
        }
        return;
    }

    console.log(renderConfig(config));
}

main();

export {};
