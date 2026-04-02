# This helper example focuses on contrasting two sorting behaviors without extra setup noise.

# This extra example extends sorting-and-searching with tie-order comparisons.

# Keep this helper separate so the main example can focus on the larger idea without extra noise.
def print_records(records, title):
    print(title)
    for record in records:
        print(f"- score={record['score']}, name={record['name']}")
    print()


records = [
    {"score": 90, "name": "Ana"},
    {"score": 75, "name": "Bob"},
    {"score": 90, "name": "Carla"},
    {"score": 75, "name": "Diego"},
    {"score": 90, "name": "Emma"},
]

print_records(records, "Original order:")

stable = sorted(records, key=lambda record: record["score"])
print_records(stable, "After sorted(...) by score (stable):")

reordered_ties = sorted(records, key=lambda record: (record["score"], record["name"]))
print_records(reordered_ties, "After sorted(...) with explicit tie-breaker:")

print("Python's sort is stable. Tie-breakers can still change the order of equal scores.")
