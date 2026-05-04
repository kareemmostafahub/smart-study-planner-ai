"""
API Routes - Smart Study Planner

This module exposes endpoints for:
- Creating study plans
- Generating schedules
- Optimizing results
- Testing scheduler engine
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from backend.scheduler.core import StudyTask, StudyScheduler
from backend.scheduler.optimizer import ScheduleOptimizer

# --------------------------------------------------
# Router
# --------------------------------------------------
router = APIRouter()

# --------------------------------------------------
# Request Models
# --------------------------------------------------
class TaskInput(BaseModel):
    subject: str
    difficulty: int  # 1 - 5
    hours_needed: float
    deadline: str  # YYYY-MM-DD


class ScheduleRequest(BaseModel):
    daily_hours: float
    tasks: List[TaskInput]

# --------------------------------------------------
# Health Check
# --------------------------------------------------
@router.get("/health")
async def api_health():
    return {
        "status": "ok",
        "message": "API is working properly"
    }

# --------------------------------------------------
# Generate Schedule
# --------------------------------------------------
@router.post("/generate-schedule")
async def generate_schedule(request: ScheduleRequest):
    try:
        # Convert input to StudyTask objects
        tasks = [
            StudyTask(
                subject=t.subject,
                difficulty=t.difficulty,
                hours_needed=t.hours_needed,
                deadline=t.deadline
            )
            for t in request.tasks
        ]

        # Core scheduler
        scheduler = StudyScheduler(daily_hours=request.daily_hours)
        raw_schedule = scheduler.generate_schedule(tasks)

        # Optimization layer
        optimizer = ScheduleOptimizer(max_daily_hours=request.daily_hours)
        optimized_schedule = optimizer.optimize(raw_schedule)

        return {
            "success": True,
            "data": optimized_schedule,
            "meta": {
                "total_tasks": len(tasks),
                "daily_limit": request.daily_hours
            }
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --------------------------------------------------
# Test Endpoint (for debugging)
# --------------------------------------------------
@router.get("/test")
async def test_example():
    return {
        "message": "Scheduler system is ready",
        "example": {
            "subject": "Math",
            "difficulty": 4,
            "hours_needed": 10,
            "deadline": "2026-06-01"
        }
    }
