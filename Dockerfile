# Use an official Python runtime based on Debian 10 "buster" as a parent image.
FROM python:3.8.1-slim-buster

# Set some environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Install system packages required by Wagtail and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libwebp-dev \
    gettext \
 && rm -rf /var/lib/apt/lists/*

# Setup workdir
RUN mkdir /src
WORKDIR /src

# Python dependencies
COPY requirements.txt /src/
COPY test-requirements.txt /src/
RUN pip install -r /src/requirements.txt
RUN pip install -r /src/test-requirements.txt

# Copy the project files
COPY .coveragerc .
COPY apps/ apps/
COPY project_name/ project_name/
COPY manage.py .
COPY scripts/ scripts/
