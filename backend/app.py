"""
Smart Study Planner API - Backend Entry Point

Modern FastAPI architecture with:
- Clean modular design
- Dependency-ready structure
- Structured logging
- Middleware for performance tracking
- Global exception handling
- API versioning support
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
import logging

# Routes
from backend.routes.api import router as api_router

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger("smart_study_planner")

# --------------------------------------------------
# App Initialization
# --------------------------------------------------
app = FastAPI(
    title="Smart Study Planner API",
    description="AI-powered intelligent study scheduling system",
    version="1.0.0",
)

# --------------------------------------------------
# CORS Middleware
# --------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Performance Logging Middleware
# --------------------------------------------------
@app.middleware("http")
async def performance_middleware(request: Request, call_next):
    start = time.time()

    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    duration = time.time() - start
    logger.info(f"Response time: {duration:.4f}s")

    return response

# --------------------------------------------------
# Global Exception Handler
# --------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled Exception: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
        },
    )

# --------------------------------------------------
# Health Check
# --------------------------------------------------
@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "Smart Study Planner API"
    }

# --------------------------------------------------
# Root
# --------------------------------------------------
@app.get("/")
async def root():
    return {
        "message": "Smart Study Planner API is running",
        "version": "1.0.0"
    }

# --------------------------------------------------
# API Routes
# --------------------------------------------------
app.include_router(api_router, prefix="/api/v1")
