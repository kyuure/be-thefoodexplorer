# syntax=docker/dockerfile:1

# Use python image
FROM python:3.8-slim-buster

# Environment setup, if any

# Run dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the code to /app
WORKDIR /app
COPY app.py .
COPY scr/ .

# Run the app
CMD ["ls"]
CMD ["ls", "scr/"]
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
