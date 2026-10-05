habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True),
    ("Study AI", True)
]

for habit, completed in habits:
    if completed:
        print(f"{habit}: Done")
    else:
        print(f"{habit}: Not done")


def habit_report(habits):
    completed = sum(1 for habit, status in habits if status)

    return {
        "completed": completed,
        "total": len(habits)
    }


print(habit_report(habits))