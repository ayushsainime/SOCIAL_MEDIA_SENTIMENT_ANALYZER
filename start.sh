#!/bin/bash

# Start FastAPI backend in background (internal service).
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &

# Start Reflex in production single-port mode for deployment.
reflex run --env prod --single-port --backend-host 0.0.0.0 --backend-port 3000
