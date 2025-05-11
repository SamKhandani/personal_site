FROM python:3.9.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create and set permissions for database directory
RUN mkdir -p /var/www \
    && chown -R www-data:www-data /var/www

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make scripts executable
RUN chmod +x scripts/create_superuser_and_push.sh

# Run migrations and create superuser
RUN ./scripts/create_superuser_and_push.sh

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port available to the world outside this container
EXPOSE $PORT

# Run gunicorn
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT 