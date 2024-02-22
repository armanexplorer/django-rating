# Use the official Python image as the base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the project dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY project /app

# Expose the port on which Gunicorn will listen
EXPOSE 8000

# Run Gunicorn with the specified configuration
CMD ["gunicorn", "-c", "gunicorn.conf.py"]