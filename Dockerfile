# Dockerfile for HuggingFace Spaces
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies needed by ML wheels/runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Reflex first: it manages pydantic/sqlmodel compatibility
RUN pip install --no-cache-dir reflex==0.8.28.post1

# Install remaining Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Copy application code
COPY . .

EXPOSE 3000

# Run directly: avoids CRLF issues with start.sh on Windows
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & reflex run --frontend-port 3000 --backend-port 8001"]
