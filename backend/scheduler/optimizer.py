"""
Optimizer Module - Smart Study Planner

This module enhances the core scheduler by:
- Improving time distribution efficiency
- Reducing overload (burnout prevention)
- Balancing difficulty across days
- Applying heuristic optimization strategies
"""

from typing import List, Dict, Any
import copy


class ScheduleOptimizer:
    """
    Applies optimization layer over raw schedule output
    """

    def __init__(self, max_daily_hours: float = 8.0):
        self.max_daily_hours = max_daily_hours

    def balance_workload(self, schedule: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Prevents overloading specific days by redistributing tasks
        """

        optimized = copy.deepcopy(schedule)
        daily_load = {}

        # Calculate daily load
        for item in optimized:
            day = item["date"]
            daily_load[day] = daily_load.get(day, 0) + item["hours"]

        # Adjust overloads
        for item in optimized:
            day = item["date"]

            if daily_load[day] > self.max_daily_hours:
                excess = daily_load[day] - self.max_daily_hours

                reduce_by = min(item["hours"], excess * 0.5)

                item["hours"] -= reduce_by
                daily_load[day] -= reduce_by

        return optimized

    def smooth_transitions(self, schedule: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Ensures gradual difficulty transitions between days
        (simulates adaptive learning behavior)
        """

        for i in range(1, len(schedule)):
            prev = schedule[i - 1]
            curr = schedule[i]

            # If same subject continues too hard, smooth it
            if prev["subject"] == curr["subject"]:
                curr["hours"] *= 0.9  # slight reduction for fatigue handling

        return schedule

    def optimize(self, schedule: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Main optimization pipeline
        """

        schedule = self.balance_workload(schedule)
        schedule = self.smooth_transitions(schedule)

        return schedule
