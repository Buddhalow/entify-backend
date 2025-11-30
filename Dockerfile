# Use the official Python runtime image
FROM python:3.11.13-slim AS base

# Create the app directory
RUN mkdir /app

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    lib32z1-dev \
    zlib1g-dev \
    python3-dev \
    python3-lxml \
    python3-numpy \
    libpython3.13-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables 
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project  and install dependencies
COPY requirements.txt  /app/
 
# run this command to install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project to the container
COPY . /app/

EXPOSE 8000
 
# Run Django’s development server
ENTRYPOINT ["python", "manage.py", "runserver"]

CMD ["0.0.0.0:8000"]