# Use an official Python base image
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy only what is necessary first (for build caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app files
COPY . .

# Expose port (FastAPI default is 8000)
EXPOSE 8000

# Command to run the FastAPI app; adjust path if needed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
