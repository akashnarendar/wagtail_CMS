# Use a lightweight modern Python
FROM python:3.11-slim

# System config
ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt gunicorn

# Copy the project code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Default command: run migrations and start the server
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn mysite.wsgi:application --bind 0.0.0.0:8000"]
