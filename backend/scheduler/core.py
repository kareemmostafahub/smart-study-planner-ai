"""
Core Scheduling Engine - Smart Study Planner

This module is responsible for:
- Converting raw study input into structured tasks
- Prioritizing subjects based on urgency and difficulty
- Generating optimized study sessions
- Providing a scalable scheduling core (algorithm layer)
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any


class StudyTask:
    """
    Represents a single study unit/task
    """
    def __init__(self, subject: str, difficulty: int, hours_needed: float, deadline: str):
        self.subject = subject
        self.difficulty = difficulty  # 1 (easy) → 5 (hard)
        self.hours_needed = hours_needed
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")

    def urgency_score(self) -> float:
        """
        Calculates urgency based on deadline proximity + difficulty
        """
        days_left = (self.deadline - datetime.now()).days
        days_left = max(days_left, 1)

        return (self.difficulty * 2) + (100 / days_left)


class StudyScheduler:
    """
    Core scheduling algorithm engine
    """

    def __init__(self, daily_hours: float):
        self.daily_hours = daily_hours

    def prioritize_tasks(self, tasks: List[StudyTask]) -> List[StudyTask]:
        """
        Sort tasks based on urgency score (descending)
        """
        return sorted(tasks, key=lambda t: t.urgency_score(), reverse=True)

    def generate_schedule(self, tasks: List[StudyTask]) -> List[Dict[str, Any]]:
        """
        Generates optimized daily study schedule
        """

        sorted_tasks = self.prioritize_tasks(tasks)
        schedule = []

        current_date = datetime.now()
        remaining_hours = self.daily_hours

        for task in sorted_tasks:
            hours = task.hours_needed

            while hours > 0:
                if remaining_hours == 0:
                    current_date += timedelta(days=1)
                    remaining_hours = self.daily_hours

                allocated = min(hours, remaining_hours)

                schedule.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "subject": task.subject,
                    "hours": round(allocated, 2)
                })

                hours -= allocated
                remaining_hours -= allocated

        return schedule
