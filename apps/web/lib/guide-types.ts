export type Question = {
    id: string;
    prompt: string;
    options: { id: string; text: string }[];
    correct: string;
    explanation: string;
};
export type Guide = {
    moduleId: string;
    version: number;
    nextModuleId: string;
    exampleId: string;
    exerciseIds: string[];
    steps: { id: string; title: string; text: string }[];
    fragments: string[];
    preparedInput: string;
    referenceOutput: string;
    prediction: Question;
    review: Question[];
    feedback: {
        activityId: string;
        caseName: string;
        expectation: string;
        suggestion: string;
        hint: number;
    }[];
};
export type Journey = {
    id: string;
    step: string;
    reviewed: string[];
    answers: Record<string, string>;
    lastVisited: string;
};
export const journeyKey = (guide: Pick<Guide, "moduleId" | "version">) =>
    `${guide.moduleId}@${guide.version}`;
