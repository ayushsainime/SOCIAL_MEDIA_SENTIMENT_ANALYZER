# Dockerfile - Phase 7
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_sm
COPY . .
RUN chmod +x start.sh
EXPOSE 8000
EXPOSE 3000
CMD ["./start.sh"]