import os
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(
    os.path.join(BASE_DIR, "Apps")
)

SECRET_KEY = str(os.environ.get('SECRET_KEY', "ddwr&@m^@k#bh+py-r@kgff4u!h7j%nvhja(^is*1h4l!4oaq8"))

DEBUG = int(os.environ.get('DEBUG', 1))

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
 
INSTALLED_APPS +=[
    'Users',
    'Store',
    'smart_selects',
]

USE_DJANGO_JQUERY = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Configurations.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['Templates'],
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

WSGI_APPLICATION = 'Configurations.wsgi.application'

AUTH_USER_MODEL = "Users.Profile" 

LOGIN_REDIRECT_URL = 'LadingPage'

LOGIN_URL = 'ViewLogin'

# LOGOUT_URL = ''
# LOGOUT_REDIRECT_URL = ''

DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.environ.get('DB_NAME', os.path.join(BASE_DIR, 'db.sqlite3'))),
        'USER': str(os.environ.get('DB_USER', '')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD', '')),
        'HOST': str(os.environ.get('DB_HOST', '')),
        'PORT': str(os.environ.get('DB_PORT', ''))
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
