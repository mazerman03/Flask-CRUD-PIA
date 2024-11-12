# Use Python 3.9 as the base image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow connections to the Flask app
EXPOSE 5000

# Set environment variables
ENV FLASK_ENV=development

# Command to run the Flask app
CMD ["python", "app.py"]
