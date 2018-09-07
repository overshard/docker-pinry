import os

# SECURITY WARNING: keep the secret key used in production secret!
# Or just write your own secret-key here instead of using a env-variable
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# SECURITY WARNING: use your actual domain name in production!
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/data/production.db',
    }
}

# Allow users to register by themselves
ALLOW_NEW_REGISTRATIONS = True

# Delete image files once you remove your pin
IMAGE_AUTO_DELETE = True

# thumbnail size control
IMAGE_SIZES = {
    'thumbnail': {'size': [240, 0]},
    'standard': {'size': [600, 0]},
    'square': {'crop': True, 'size': [125, 125]},
}
