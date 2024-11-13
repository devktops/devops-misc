# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the application files
COPY app.py ./

# Install required libraries
RUN pip install prometheus_client psutil flask waitress werkzeug

# Expose the Prometheus port
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
