#!/bin/bash

"""
Smart Study Planner - Local Run Script
Starts backend server locally with uvicorn
"""

echo "🚀 Starting Smart Study Planner Backend..."

# Move to project root (optional safety)
cd "$(dirname "$0")/.."

# Activate virtual environment if exists
if [ -d "venv" ]; then
    echo "🔧 Activating virtual environment..."
    source venv/bin/activate
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run FastAPI server
echo "🌐 Launching API server at http://127.0.0.1:8000"
uvicorn backend.app:app --reload --host 127.0.0.1 --port 8000
