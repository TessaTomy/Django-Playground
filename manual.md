## 🛠️ Project Setup Guide

### 1. Create project folder and virtual environment
```bash
mkdir proname
cd proname
python -m venv env
env\Scripts\activate   # Windows
```

### 2. Install dependencies
```bash
pip install django mysqlclient pillow
```

---

### 3. Start Django project and app
```bash
django-admin startproject proname .
django-admin startapp adminapp
```

Inside `adminapp`, create:
- `urls.py`
- `forms.py` (optional, for forms)

---

### 4. Configure `settings.py`
Open `proname/settings.py` and update:

**Installed apps:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminapp',   # add your app here
]
```

**Templates:**
```python
import os

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

**Static files:**
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

---

### 5. Create folders
At the project root:
```
templates/
static/
```

Inside `templates/`, add `index.html`.  
Inside `static/`, add your CSS/JS/images.

---

### 6. Wire up URLs
**Project `urls.py` (proname/urls.py):**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('adminapp.urls')),  # root points to app
]
```

**App `urls.py` (adminapp/urls.py):**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

---

### 7. Define a view
**adminapp/views.py:**
```python
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
```

---

### 8. Run migrations and server
```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → you should see your `index.html`.

---
