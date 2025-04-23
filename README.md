# Personal Website

A professional personal website built with Django, featuring a modern design and admin panel for content management.

## Features

- Responsive design
- Dark/Light mode
- Admin panel for content management
- Blog system
- Contact form
- Portfolio showcase
- SEO optimized
- Analytics integration

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a .env file in the root directory with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Color Scheme

- Primary: Dark Blue (#0A192F)
- Accent: Purple Blue (#6C63FF)
- Background: Light Gray (#F5F5F5)
- Secondary Accent: Soft Yellow (#FCD34D)
- Text: Dark Gray (#1E1E1E)

## Fonts

- Vazir (Persian)
- Inter Regular (English) 