"""
Unit tests for Smart Study Planner core logic

Tests:
- StudyTask urgency calculation
- Scheduler ordering logic
- Basic schedule generation validity
"""

import pytest
from backend.scheduler.core import StudyTask, StudyScheduler


# --------------------------------------------------
# Test StudyTask urgency score
# --------------------------------------------------
def test_urgency_score_higher_for_harder_tasks():
    task_hard = StudyTask(
        subject="Math",
        difficulty=5,
        hours_needed=10,
        deadline="2026-06-01"
    )

    task_easy = StudyTask(
        subject="English",
        difficulty=2,
        hours_needed=10,
        deadline="2026-06-01"
    )

    assert task_hard.urgency_score() > task_easy.urgency_score()


# --------------------------------------------------
# Test scheduler output is not empty
# --------------------------------------------------
def test_schedule_generation_not_empty():
    tasks = [
        StudyTask("Math", 5, 10, "2026-06-01"),
        StudyTask("Physics", 4, 8, "2026-06-05")
    ]

    scheduler = StudyScheduler(daily_hours=6)
    schedule = scheduler.generate_schedule(tasks)

    assert len(schedule) > 0


# --------------------------------------------------
# Test schedule structure integrity
# --------------------------------------------------
def test_schedule_structure_valid():
    tasks = [
        StudyTask("CS", 3, 6, "2026-06-10")
    ]

    scheduler = StudyScheduler(daily_hours=6)
    schedule = scheduler.generate_schedule(tasks)

    first = schedule[0]

    assert "date" in first
    assert "subject" in first
    assert "hours" in first
