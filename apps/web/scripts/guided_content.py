"""Validate authored journeys against the generated, canonical curriculum."""

import copy


def attach_guides(guides, docs, activities):
    try:
        _attach_guides(guides, docs, activities)
    except (KeyError, TypeError, AttributeError) as error:
        raise ValueError("Incomplete or malformed guided content") from error


def _attach_guides(guides, docs, activities):
    documents = {doc["id"]: doc for doc in docs}
    seen = set()
    for authored in guides:
        guide = copy.deepcopy(authored)
        module = guide["moduleId"]
        if module in seen or module not in documents:
            raise ValueError("Duplicate or unknown guided module")
        seen.add(module)
        if not isinstance(guide["version"], int) or guide["version"] < 1:
            raise ValueError("A positive pedagogical version is required")
        if guide["nextModuleId"] not in documents:
            raise ValueError("Unknown next module")
        ids = [guide["exampleId"], *guide["exerciseIds"]]
        if len(set(ids)) != 3 or set(ids) != set(documents[module]["activities"]):
            raise ValueError("Journey must reference this module's three activities")
        if activities[ids[0]]["kind"] != "example" or any(
            activities[id]["kind"] != "exercise" for id in ids[1:]
        ):
            raise ValueError("Invalid journey activity kinds")
        if [s["id"] for s in guide["steps"]] != [
            "understand",
            "predict",
            "run",
            "modify",
            "solve",
            "review",
        ] or any(not s["title"].strip() or not s["text"].strip() for s in guide["steps"]):
            raise ValueError("Incomplete or duplicate journey steps")
        questions = [guide["prediction"], *guide["review"]]
        if len(guide["review"]) != 3 or len({q["id"] for q in questions}) != 4:
            raise ValueError("Incomplete or duplicate questions")
        for q in questions:
            options = q["options"]
            option_ids = {o["id"] for o in options}
            if (
                not q["id"]
                or not q["prompt"].strip()
                or not q["explanation"].strip()
                or len(options) < 2
                or len(option_ids) != len(options)
                or q["correct"] not in option_ids
                or any(not o["id"] or not o["text"].strip() for o in options)
            ):
                raise ValueError("Incomplete question or answer")
        fragments = []
        for prefix in guide.pop("fragmentPrefixes"):
            matches = [
                line
                for line in activities[ids[0]]["source"].splitlines()
                if line.startswith(prefix)
            ]
            if len(matches) != 1:
                raise ValueError("Example fragment is missing or ambiguous")
            fragments.append(matches[0])
        guide["fragments"] = fragments
        if not fragments or not guide["preparedInput"] or not guide["referenceOutput"]:
            raise ValueError("Missing learning scenario")
        feedback_seen = set()
        for tip in guide["feedback"]:
            activity = tip["activityId"]
            key = (activity, tip["caseName"])
            if (
                activity not in ids[1:]
                or key in feedback_seen
                or tip["caseName"] not in {c["name"] for c in activities[activity]["cases"]}
                or not tip["expectation"].strip()
                or not tip["suggestion"].strip()
                or tip["hint"] not in range(1, len(activities[activity]["hints"]) + 1)
            ):
                raise ValueError("Invalid or duplicate feedback reference")
            feedback_seen.add(key)
        expected = {(id, c["name"]) for id in ids[1:] for c in activities[id]["cases"]}
        if feedback_seen != expected:
            raise ValueError("Missing case feedback")
        documents[module]["guide"] = guide
