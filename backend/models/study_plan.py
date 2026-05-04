"""
Study Plan Data Models

This module defines the core data structures used across the system:
- StudyTask representation
- StudyPlan aggregation model
- Validation-ready structures for scaling API and DB integration
"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


# --------------------------------------------------
# Single Study Task Model
# --------------------------------------------------
class StudyTaskModel(BaseModel):
    subject: str = Field(..., min_length=1, max_length=100)
    difficulty: int = Field(..., ge=1, le=5)
    hours_needed: float = Field(..., gt=0)
    deadline: str  # YYYY-MM-DD format


# --------------------------------------------------
# Generated Study Session Model
# --------------------------------------------------
class StudySession(BaseModel):
    date: str
    subject: str
    hours: float


# --------------------------------------------------
# Full Study Plan Model
# --------------------------------------------------
class StudyPlan(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    total_tasks: int
    daily_limit: float
    sessions: List[StudySession]
    optimized: bool = True
