from pathlib import Path
import pymysql
import os
from root.applist import *


pymysql.install_as_MySQLdb()
BASE_DIR = Path(__file__).resolve().parent.parent


# ================================================================= #
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = True if os.getenv('DJANGO_DEBUG', 'False') == 'True'  else False 

SOCKET_URL=os.getenv('SOCKET_URL')

ADSPECT_API_KEY=os.getenv('ADSPECT_API_KEY')

BASE_URL=os.getenv('BASE_URL')

TIME_ZONE='Asia/Kolkata'

DJANGO_USER_MAX_LOG_SIZE = int(os.getenv('DJANGO_USER_MAX_LOG_SIZE'))

Bytes_number = int(os.getenv('DJANGO_LOG_MB'))
backupCount = int(os.getenv('DJANGO_LOG_BACKUP'))


MYSQL_USERNAME=os.getenv('MYSQL_USERNAME')
MYSQL_ROOT_PASSWORD=os.getenv('MYSQL_ROOT_PASSWORD')
MYSQL_HOST=os.getenv('MYSQL_HOST')
MYSQL_PORT=os.getenv('MYSQL_PORT')
MYSQL_DATABASE=os.getenv('MYSQL_DATABASE')

# ================================================================= #

os.makedirs(BASE_DIR / 'logs', exist_ok=True)
os.makedirs(BASE_DIR / 'media', exist_ok=True)
os.makedirs(BASE_DIR / 'static', exist_ok=True)
os.makedirs(BASE_DIR / 'static_files', exist_ok=True)
os.makedirs(BASE_DIR / 'temp', exist_ok=True)

ALLOWED_HOSTS = ["*"]

SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
]

INSTALLED_APPS = SYSTEM_APPS+INSTALL_APPS+CREATED_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accountapp.middlewares.UserActivityMiddleware',
    'app.middleware.Enforce2FAMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

ROOT_URLCONF = 'root.urls'
ASGI_APPLICATION = 'root.asgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DATABASE,
        'USER': MYSQL_USERNAME,
        'PASSWORD': MYSQL_ROOT_PASSWORD,
        'HOST': MYSQL_HOST,
        'PORT': MYSQL_PORT,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
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

APPEND_SLASH = True
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' 

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static_files',  
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static') 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_TRUSTED_ORIGINS = [BASE_URL]

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/" 

LOG_FILE_PATH = BASE_DIR / 'logs' / 'django.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(levelname)s %(asctime)s %(module)s %(message)s',
            'log_colors': {
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    'handlers': {
        'rotating_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOG_FILE_PATH,
            'maxBytes': 1024 * 1024 * Bytes_number,
            'backupCount': backupCount,
            'level': 'DEBUG',
            'formatter': 'verbose',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'colored' if DEBUG else 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['rotating_file', 'console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['rotating_file', 'console'],
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'propagate': False,
        },
    },
}