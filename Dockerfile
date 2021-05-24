# syntax=docker/dockerfile:1

# Use python image
FROM python:3.8

# Environment setup, if any

# Run dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the code to /app
WORKDIR /app
COPY app.py .
COPY scr/ .

# Run the app
ENTRYPOINT ["python"]
CMD ["app.py"]
