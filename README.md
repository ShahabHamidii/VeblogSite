## What this is
A small Django-based blog application (Veblog) with user accounts, post publishing, comments, likes, and a contact/message model — intended as a simple personal/blogging site and admin-backed content manager.

### Stack
- **Language(s):** Python (backend) with front-end assets in JavaScript, CSS, SCSS and HTML
- **Framework / runtime:** Django 5.2.x (project created with Django 5.2.5)
- **Notable libraries:** django-cleanup, django-social-share, django-widget-tweaks, Pillow (ImageField support)

## How it's organized
```
Veblog/               Django project settings, URLs, WSGI
accounts/             user Profile model and account-related views/templates
blog/                 blog models (Post, Category, Comment, Message, Like), views, forms
home_app/             home page view (lists posts) and related templates
templates/            project-wide templates (index, post detail, blog lists, contact, etc.)
assets/               static assets (JS, CSS, images) used by templates
media/                uploaded media (profile pictures, post images)
context_processors/   custom context processor (recent posts)
db.sqlite3            committed SQLite database (development/demo)
manage.py             Django entry point (runserver, migrations, admin, etc.)
.idea/                IDE/editor files (local)
```

How it fits together:
- Veblog is a standard Django project. The project-level settings (Veblog/settings.py) wire template dirs, static/media roots, and installed apps.
- Three main apps implement features: accounts (Profile), blog (posts, comments, likes, messages), and home_app (landing page). Templates render HTML pages and use assets/ for CSS/JS. Views in blog implement post listing, search, details, AJAX-like like/unlike endpoints returning JSON, and CRUD for messages.

## How to run it
The shortest path to run locally (development):

1. Clone and create a virtual environment
```
git clone https://github.com/ShahabHamidii/VeblogSite.git
cd VeblogSite
python -m venv .venv
# on macOS/Linux
source .venv/bin/activate
# on Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

2. Install dependencies
- If a requirements.txt exists use:
```
pip install -r requirements.txt
```
- If not, install the obvious dependencies:
```
pip install "Django==5.2.5" django-cleanup django-social-share django-widget-tweaks Pillow
```

3. Prepare the database and run migrations (this project includes a db.sqlite3 for development/demo)
```
python manage.py migrate
python manage.py createsuperuser   # optional: create admin user
```

4. (Optional) Collect static files for production-like testing
```
python manage.py collectstatic
```

5. Run the development server
```
python manage.py runserver
```

Then open http://127.0.0.1:8000/ to view the site. Notes:
- Settings currently have DEBUG = True and a hard-coded SECRET_KEY in Veblog/settings.py — do not use as-is for production.
- MEDIA and STATIC serve from MEDIA_ROOT (media/) and STATICFILES_DIRS (assets/) in development. Uploaded images (ImageField) require Pillow.
