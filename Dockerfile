# Use official Python image as base
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
