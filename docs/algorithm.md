# 🧠 Smart Study Planner - Algorithm Design

## 📌 Overview
This document explains the core algorithms used in the Smart Study Planner system.  
The goal is to transform raw study tasks into an optimized, balanced, and realistic schedule.

---

## ⚙️ 1. Task Prioritization Algorithm

Each study task is assigned a priority score based on:
- Difficulty level (1–5)
- Deadline proximity
- Required study hours

### Urgency Formula:
Urgency Score = (Difficulty × 2) + (100 / Days Left)

### Explanation:
- Higher difficulty → higher priority
- Closer deadline → exponentially higher urgency
- Ensures time-critical subjects are handled first

---

## 📅 2. Scheduling Algorithm (Greedy Allocation)

After sorting tasks by urgency:

Process:
1. Sort tasks descending by urgency score
2. Start from current day
3. Allocate study hours sequentially
4. Fill each day up to available limit
5. Move overflow to next day

Strategy:
This is a Greedy Algorithm because it always selects the most urgent task first, making locally optimal choices that build a globally efficient schedule.

---

## ⚖️ 3. Optimization Algorithm

After initial schedule generation, optimization is applied:

Goals:
- Prevent overload on any single day
- Smooth learning distribution
- Reduce cognitive fatigue

Techniques:

1. Load Balancing  
If daily hours exceed limit:
- Reduce allocation proportionally
- Redistribute excess to next days

2. Session Smoothing  
If same subject repeats:
- Reduce continuous load
- Prevent mental fatigue

---

## 🔄 4. Data Flow

Input Tasks → Compute Urgency Score → Sort by Priority → Greedy Scheduling → Load Balancing → Smoothing Optimization → Final Study Plan

---

## 🧠 5. Complexity Analysis

Time Complexity:
- Sorting: O(n log n)
- Scheduling: O(n × d)
- Optimization: O(n)

Where:
- n = number of tasks
- d = number of days

---

## 🎯 6. Why This Approach?

This system simulates:
- Real human planning behavior
- Deadline-driven prioritization
- Energy-aware study distribution

It is not just a scheduler — it is a decision-making system.

---

## 🚀 7. Future Improvements

- Machine Learning-based priority scoring
- Adaptive scheduling based on user performance
- Reinforcement learning optimization
- Personalized fatigue modeling

---

## 💡 Summary

The algorithm combines:
- Greedy strategy
- Heuristic scoring
- Load balancing optimization

to generate a realistic and efficient study plan.
