# This extra example extends formatted output with a compact score report.
# Example purpose: align labels, numbers, and a final summary row.

students = [
    ("Ana", 91, 4),
    ("Bruno", 77, 3),
    ("Carla", 88, 5),
]

print(f"{'Student':<10}{'Score':>8}{'Tasks':>8}{'Average':>10}")
print("-" * 36)

weighted_total = 0
task_total = 0
for name, score, tasks in students:
    average = score / tasks
    weighted_total += score
    task_total += tasks
    print(f"{name:<10}{score:>8}{tasks:>8}{average:>10.2f}")

print("-" * 36)
print(f"{'Totals':<10}{weighted_total:>8}{task_total:>8}{weighted_total / task_total:>10.2f}")
