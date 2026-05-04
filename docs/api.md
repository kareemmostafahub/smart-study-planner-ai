# 🌐 Smart Study Planner - API Documentation

## 📌 Overview
This document describes all available REST API endpoints for the Smart Study Planner backend system.

Base URL:
http://localhost:8000/api/v1

---

## 🔍 1. Health Check

### Endpoint:
GET /health

### Description:
Checks if the API server is running.

### Response:
{
  "status": "ok",
  "message": "API is working properly"
}

---

## 📊 2. Generate Study Schedule

### Endpoint:
POST /generate-schedule

### Description:
Generates an optimized study plan based on tasks, difficulty, and deadlines.

### 📥 Request Body:
{
  "daily_hours": 6,
  "tasks": [
    {
      "subject": "Math",
      "difficulty": 5,
      "hours_needed": 10,
      "deadline": "2026-06-10"
    },
    {
      "subject": "Physics",
      "difficulty": 4,
      "hours_needed": 8,
      "deadline": "2026-06-08"
    }
  ]
}

### 📤 Response:
{
  "success": true,
  "data": [
    {
      "date": "2026-05-05",
      "subject": "Math",
      "hours": 3.5
    },
    {
      "date": "2026-05-06",
      "subject": "Physics",
      "hours": 4
    }
  ],
  "meta": {
    "total_tasks": 2,
    "daily_limit": 6
  }
}

---

## 🧪 3. Test Endpoint

### Endpoint:
GET /test

### Description:
Returns sample data for debugging and testing API connectivity.

### Response:
{
  "message": "Scheduler system is ready",
  "example": {
    "subject": "Math",
    "difficulty": 4,
    "hours_needed": 10,
    "deadline": "2026-06-01"
  }
}

---

## ⚙️ Error Handling

### Standard Error Response:
{
  "success": false,
  "error": "Internal Server Error"
}

---

## 🔐 Notes

- All endpoints are under /api/v1
- Input validation is handled using Pydantic models
- CORS is enabled for frontend integration
- Designed for scalability and future authentication support

---

## 🚀 Future Extensions

- User authentication (JWT)
- Save study plans to database
- User progress tracking
- AI-based adaptive scheduling
