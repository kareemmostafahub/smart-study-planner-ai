/**
 * Smart Study Planner - Frontend Logic
 * Handles:
 * - Task creation
 * - UI state management
 * - API communication with backend
 * - Rendering optimized schedule
 */

const API_URL = "http://localhost:8000/api/v1";

let tasks = [];

// --------------------------------------------------
// DOM Elements
// --------------------------------------------------
const taskForm = document.getElementById("taskForm");
const taskList = document.getElementById("taskList");
const resultDiv = document.getElementById("result");
const generateBtn = document.getElementById("generateBtn");

// --------------------------------------------------
// Add Task
// --------------------------------------------------
taskForm.addEventListener("submit", (e) => {
    e.preventDefault();

    const subject = document.getElementById("subject").value;
    const difficulty = document.getElementById("difficulty").value;
    const hours = document.getElementById("hours").value;
    const deadline = document.getElementById("deadline").value;

    const task = {
        subject,
        difficulty: parseInt(difficulty),
        hours_needed: parseFloat(hours),
        deadline
    };

    tasks.push(task);
    renderTasks();
    taskForm.reset();
});

// --------------------------------------------------
// Render Tasks
// --------------------------------------------------
function renderTasks() {
    taskList.innerHTML = "";

    tasks.forEach((task, index) => {
        const li = document.createElement("li");

        li.innerHTML = `
            <strong>${task.subject}</strong>
            | Difficulty: ${task.difficulty}
            | Hours: ${task.hours_needed}
            | Deadline: ${task.deadline}
            <button onclick="removeTask(${index})">❌</button>
        `;

        taskList.appendChild(li);
    });
}

// --------------------------------------------------
// Remove Task
// --------------------------------------------------
function removeTask(index) {
    tasks.splice(index, 1);
    renderTasks();
}

// --------------------------------------------------
// Generate Schedule (API Call)
// --------------------------------------------------
generateBtn.addEventListener("click", async () => {
    if (tasks.length === 0) {
        alert("Please add at least one task!");
        return;
    }

    const payload = {
        daily_hours: 6,
        tasks: tasks
    };

    try {
        const response = await fetch(`${API_URL}/generate-schedule`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.success) {
            renderSchedule(data.data);
        } else {
            resultDiv.innerHTML = "Error generating schedule";
        }

    } catch (error) {
        console.error(error);
        resultDiv.innerHTML = "Server error. Make sure backend is running.";
    }
});

// --------------------------------------------------
// Render Optimized Schedule
// --------------------------------------------------
function renderSchedule(schedule) {
    resultDiv.innerHTML = "";

    schedule.forEach(item => {
        const div = document.createElement("div");
        div.className = "schedule-item";

        div.innerHTML = `
            <p><strong>Date:</strong> ${item.date}</p>
            <p><strong>Subject:</strong> ${item.subject}</p>
            <p><strong>Hours:</strong> ${item.hours}</p>
        `;

        resultDiv.appendChild(div);
    });
}
