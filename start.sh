#!/bin/bash

# Start FastAPI backend in background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Reflex frontend in foreground
cd frontend && reflex run --port 3000 --host 0.0.0.0