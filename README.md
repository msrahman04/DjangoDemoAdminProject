# DjangoDemoAdminProject
# 🛠️ Virtualenv and Django Project Setup Guide

A comprehensive guide to Python virtual environment management and Django project setup.

## 📋 Contents

- [Overview](#overview)
- [Installation](#installation)
- [Essential Commands](#essential-commands)
- [Python Version Management](#python-version-management)
- [Django Setup](#django-setup)
- [Advanced Usage](#advanced-usage)
- [Configuration](#configuration)
- [Uninstallation](#uninstallation)

## 📌 Overview

### What is `virtualenv`?

`virtualenv` creates isolated Python environments, allowing you to manage project dependencies separately without conflicts between projects.

### What is `virtualenvwrapper`?

`virtualenvwrapper` extends `virtualenv` with convenient commands to manage multiple virtual environments easily. It stores all environments in one location and provides simple commands for creation, switching, and deletion.

## 💿 Installation

```bash
# Install both tools
pip install virtualenv virtualenvwrapper

# Verify installation
virtualenv --version
virtualenvwrapper --version
```

### Create and activate a new environment

`mkvirtualenv DjangoDemoPy310`

## 🌐 Django Setup

### Installing Django

```bash
# Activate your virtual environment (if not already active)
workon DjangoDemoPy310

#Upgrade pip version before install django
pip install --upgrade pip

# Install Django
pip install django

# Verify installation
python -m django --version

# If not work on python then use python3
python3 -m django --version
# Or we can use django command
django-admin --version
```

### Creating a Django Project

```bash
# Create a new Django project
django-admin startproject headphoneadmin

# Navigate to project directory
cd headphoneadmin
```

### Apply Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Viewing Migration Status
### To see which migrations have been applied:
```bash
bashpython manage.py showmigrations
```
This will show you all migrations, including the built-in ones, with a checkmark (✓) next to those that have been applied.



### Create a Django Superuser

#### Step 1: Make sure your Django server is stopped
Press Ctrl + C if the server is running

#### Step 2: Create a superuser account
```bash
# Create admin user
python manage.py createsuperuser
```

#### Step 3: Follow the prompts
You'll be asked to enter:

Username: Choose any username (e.g., admin, shahinur, etc.)
Email address: Enter your email (can be left blank)
Password: Enter a secure password
Password confirmation: Confirm your password

Example interaction:
Username (leave blank to use 'shahinurrahman'): admin
Email address: your_email@example.com
Password: ********
Password (again): ********
Superuser created successfully.

#### Step 4: Start the server again
```bash
python manage.py runserver
```

#### Step 5: Access admin panel
Go to: http://127.0.0.1:8000/admin/
Use the username and password you just created.
Alternative: If you already have a superuser
If you already created a superuser but forgot the credentials:
Reset existing superuser password:
```bash
python manage.py changepassword your_username
```
Or create another superuser:
```bash
python manage.py createsuperuser
```

### Creating a Django App

```bash
# Create a new app
python manage.py startapp products
```

### Configure Settings

Edit `headphoneadmin/settings.py` to add your app:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',  # Add your app here
]
```

### Create Models

Edit `products/models.py`:

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Headphone(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='headphones')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
```

### Configure Admin

Edit `products/admin.py`:

```python
from django.contrib import admin
from .models import Category, Headphone

# Customize the admin site
admin.site.site_header = "Headphone Admin"
admin.site.site_title = "Headphone Admin Portal"
admin.site.index_title = "Welcome to Headphone Admin Portal"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Headphone)
class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'category', 'price', 'stock')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'model', 'description')
```
### Apply Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```


### Run the Development Server

```bash
# Start the server
python manage.py runserver
```

Access the admin interface at: http://127.0.0.1:8000/admin/

### Install Additional Dependencies

```bash
# For image handling (if needed)
pip install Pillow

# Save your dependencies
pip freeze > requirements.txt
```


### Environment Variables

Set persistent environment variables in your virtual environment:

```bash
# In an active environment
echo 'export DEBUG=True' >> $VIRTUAL_ENV/bin/postactivate
echo 'unset DEBUG' >> $VIRTUAL_ENV/bin/predeactivate
```

## ⚙️ Configuration

Add to your shell configuration file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
# Virtualenvwrapper settings
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=$(which python3)
source $(which virtualenvwrapper.sh)
```

Then reload your configuration:

```bash
source ~/.zshrc  # or ~/.zshrc
```

## 🚮 Uninstallation

Complete removal of virtualenv and virtualenvwrapper:

```bash
# Uninstall packages
pip uninstall virtualenvwrapper virtualenv

# Remove environment directory (optional)
rm -rf ~/.virtualenvs
```

Also remove the configuration lines from your shell configuration file.

## 📖 References

- [Virtualenv Documentation](https://virtualenv.pypa.io/en/latest/)
- [Virtualenvwrapper Documentation](https://virtualenvwrapper.readthedocs.io/en/latest/)

---




## Environments Setup for package managements

We have created an Environments folted withe three base.txt, dev.txt and prod.txt where we can manage our custom package.

```bash
# Install packages for dev file
pip install -r requirments/dev.txt

```
