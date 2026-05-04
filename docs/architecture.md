# 🧠 Smart Study Planner - System Architecture

## 📌 Overview
Smart Study Planner is a full-stack system designed to generate optimized study schedules based on subject difficulty, deadlines, and available daily time.  
The system applies algorithmic scheduling + optimization heuristics to simulate intelligent planning.

---

## 🏗️ High-Level Architecture

The system is divided into 3 main layers:

### 1. Frontend Layer
- Built with: HTML, CSS, JavaScript
- Responsibilities:
  - User input collection (tasks, deadlines, difficulty)
  - Displaying generated study schedule
  - Sending API requests to backend

---

### 2. Backend Layer
- Built with: FastAPI (Python)

Responsibilities:
- API request handling
- Input validation using Pydantic models
- Connecting frontend with core logic
- Error handling and logging

Main modules:
- app.py → API entry point
- routes/api.py → REST endpoints

---

### 3. Core Logic Layer (Brain of the system)

This is the most important part of the system:

Scheduler (core.py):
- Converts tasks into structured schedule
- Uses priority-based algorithm:
  - urgency = difficulty + deadline proximity
- Sorts tasks and distributes study time

Optimizer (optimizer.py):
- Improves generated schedule
- Prevents overload per day
- Applies smoothing for better learning balance

---

## ⚙️ Data Flow

User Input (Frontend) → API Request (FastAPI) → Validation (Pydantic Models) → Scheduler Engine (core.py) → Optimization Layer (optimizer.py) → Final Schedule Response → Frontend Display

---

## 🧠 Algorithm Design

### Priority Scoring Logic:
- Higher difficulty → higher priority
- Closer deadline → higher urgency

### Optimization Strategy:
- Balance daily workload
- Avoid cognitive overload
- Smooth repeated subject sessions

---

## 📦 Tech Stack

- Frontend: HTML, CSS, JavaScript  
- Backend: FastAPI (Python)  
- Validation: Pydantic  
- Testing: Pytest  
- CI Ready: GitHub Actions (optional)  
- Architecture Style: Layered modular design  

---

## 🎯 Design Goals

- Simplicity with scalability  
- Clean separation of concerns  
- Extensible architecture for AI upgrades  
- Real-world engineering structure  

---

## 🚀 Future Improvements

- Machine Learning-based scheduling  
- User performance tracking  
- Database integration (PostgreSQL / MongoDB)  
- Authentication system  
- Mobile app version  

---

## 💡 Summary

This project demonstrates:
- Algorithmic thinking  
- System design skills  
- Full-stack integration  
- Real-world problem solving approach
