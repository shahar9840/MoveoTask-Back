# Use the specified Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Install necessary dependencies using pip
RUN pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Cors flask-socketio flask-jwt-extended Flask-Bcrypt eventlet

# Copy the project files into the working directory
COPY . .

# Expose the port your application will run on
EXPOSE 5000

# Command to run the Flask server
CMD ["python", "server.py"]