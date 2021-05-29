# syntax=docker/dockerfile:1

# Use python image
FROM python:3.8

# Environment setup, if any
ENV PORT 8080
ENV HOST 0.0.0.0
COPY long-indexer-312604-46a7da25596b.json .  

ENV GOOGLE_APPLICATION_CREDENTIALS="/long-indexer-312604-46a7da25596b.json"

# Run dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the code to /app
WORKDIR /app
COPY app.py .
COPY api-key.txt .
COPY src src/

# Expose port, needed in Cloud Run
EXPOSE $PORT

# Run the app
# Source: https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python#containerizing
CMD exec gunicorn -b :$PORT -w 2 --threads 8 --timeout 0 main:app
