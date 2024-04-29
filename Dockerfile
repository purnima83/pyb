# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
        python3-tk \
        xvfb

# Copy the application code into the container
COPY todo_gui.py /app/
COPY tasks.json /app/

# Set display environment variable
ENV DISPLAY=:99

# Start Xvfb and run the application
CMD Xvfb :99 -screen 0 1024x768x24 & \
    python todo_gui.py
