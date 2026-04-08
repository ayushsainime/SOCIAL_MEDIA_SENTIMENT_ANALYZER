#!/bin/bash

# Start FastAPI backend in background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Reflex app (frontend + Reflex backend) in foreground.
# Use 8001 for Reflex backend so it doesn't conflict with FastAPI on 8000.
reflex run --frontend-port 3000 --backend-port 8001
