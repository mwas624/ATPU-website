# Use the official Python image from the Docker hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app to run
EXPOSE 5000

# Set the command to run the Flask app
CMD ["python", "app.py"]
