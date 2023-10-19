# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV NGINX_VERSION 1.18.0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    supervisor

# Create and set the working directory
WORKDIR /app

# Install Flask and Gunicorn
RUN pip install Flask gunicorn gevent

# Copy the Flask application code to the container
COPY ./WebApp /app

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/sites-available/default

# Create a Supervisor configuration for Gunicorn
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 9-80 for Nginx
EXPOSE 8080

# Start Supervisor to manage the Gunicorn and Nginx processes
CMD ["/usr/bin/supervisord", "-n"]
