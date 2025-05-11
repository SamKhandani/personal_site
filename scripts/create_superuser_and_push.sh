#!/usr/bin/env bash
set -e

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser --noinput \
  --username "$DJANGO_SUPERUSER_USERNAME" \
  --email "$DJANGO_SUPERUSER_EMAIL"

# Set password for superuser
echo "from django.contrib.auth import get_user_model; \
      User = get_user_model(); \
      u = User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); \
      u.set_password('$DJANGO_SUPERUSER_PASSWORD'); u.save()" \
  | python manage.py shell

# Add and commit changes
git add .
git commit -m "Create superuser via script"
git push origin main 