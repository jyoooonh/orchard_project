"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
# config/settings/base.py
import os, json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent.parent

secret_file = os.path.join(BASE_DIR, 'secrets.json') # secrets.json 파일 위치

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")


# Build paths inside the project like this: BASE_DIR / 'subdir'.

secret_file = os.path.join(BASE_DIR, 'secrets.json')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['43.200.128.160']

# 로그인 성공 후 이동하는 URL
LOGIN_REDIRECT_URL = '/'

# 로그아웃 시 이동하는 URL
LOGOUT_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    "common.apps.CommonConfig",
    "manager.apps.ManagerConfig",
    "teacher.apps.TeacherConfig",
    "reserve.apps.ReserveConfig",
    "check.apps.CheckConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/mysite.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'reserve': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

with open('google_cloud_key.json') as f:
    google_cloud_key = json.load(f)

GOOGLE_SHEETS_CREDENTIALS = google_cloud_key
#
# GOOGLE_SHEETS_CREDENTIALS = {
#   "type": "service_account",
#   "project_id": "orchard-390906",
#   "private_key_id": "a653ce2b0ee0ebbfb68b052afb133b099be13b96",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDKSvjV578T6O+O\nT2sIY+UBQEeWOzG3FpiNmT5Wic9pHLZNrSJud/L1LIE+nrXiU5vJ9ykGbB6xXF9D\n2gMprX5TUAhUPEIIwahEVx6iXuLenDi/4qwAb8bhZhJqIi5Dmvl17st5wkF7G2Fb\nMyGw/2ePl8NKCbBXzZoh/bYORQjME0iLj7COkxCrEw6TNBCNf27pg0JJt88hdFFj\nfFAxN+p/+poDmvfZdEC7UL9yQ5CiM6pUfmOrtt7Fzt4QgO20gX1RP64HdJig0h0Z\nSuS+txEa6FvMA0jV1bBgO654za6Gvb8Z/pg4G6sjzFkxJf/d49q8UUf9AoWlD7uY\nClJZ34yLAgMBAAECggEAFWrlTZXBCpVER7JA3XKLccZ3Iytr6BE3CvGJQsBJ0BHU\n0K8z+14tFagl8ZX8ISpDpEPMJCdDrfjfB+AH1bHOCM7AaFVjkxRt1vkiVS6WoTBe\nZx0oo3iHe0sYnVlhFzyhN3XrinNMBiyv8hKdI+WRTAgACnwGykUKZ0Q6sj1ni7OO\ncGjgZC7Q6d/nk3qAgMhiwdqJBNHDfMtt7zM+BrgvYSKu6AkgbG1E4Dqs9oxSgL+M\nwj7cMe4IHN94dv4sSsjQc+Jn8hAXlIsUSLipV5q6tumr6CGHR80K7Gx+ECXuyXVH\nJDQPKf1fFta/6eEbzlrVFz5Ev2RNyyb/QSHK5L4dAQKBgQD/4dCTKNswlWlvU1gP\nUrCXSGypr3AT63mRdR4A1tXhe8tFrJV4MkF3AoUQM5qVf0oU/ltVmnuia3UKf83c\nZ2pK1O5MIKaNr4tts7u59DTJ0U11TSn5tbhR3UKjyGjrBsq8C0zZ3tdR6lwQoDdq\nnPsnjq0KJcvf5PJg27kHJQZp2QKBgQDKYtXpKiAsTuSZnXIxBb7F74DYYWit4jHX\n8ErukT/3KOez+BPxxch7sh84JxkzUwu3gi28990zr6qzDmNzW0Q8pIz2GkJfYh/9\nLZeNXSZ/To8v0ylquQsqaVDO/o+y/lLRUWFWIbVapKkZHvajPn/j5q4IAvTVMUdG\nwi6coCZnAwKBgQCj1whBIdjvS8v930S0UwMFavdA0zeVWaI2k+IJMYYzYZuvWik+\nlBc8x51B2XjynlVmCdObhVYCkoGXnmvG42S404xdrE5YzH0fWgUqtQYT73OEV0s4\nO7XwnRbtXgZn7qpjK20i17/REJmwf5XcKvXZx05fAAKBssvLXwUjYP6xSQKBgEeF\nVgLoGCaQWsjOkyQv25MnaGkPQ2bvoJ2nFVPpkKlPk1JOQP4X3xmXgODfMFCq8GER\naAh3r3wsgC52zz5c6mhj3ky6SupaSuO10PDsEka7BG7qOKC2c/Ow9BWycCXZKns+\nPx+pGeXGetudzZsy4w8u3iGGqe8NUxr2VHKVRfzxAoGBAIhoE97lUqgUTx7ohctN\n56PkQv/zPJ69MFCXXnj0yucJClmBX//fYxP9pXZ8S/lggswgiY1jSMsBXOOi022c\nAz8YIFpSfzc5WZ9GnbqemJEs61w70rYAgJ3D68ub8nLQV6XxrGbHtcHi1OD9IoUq\njZdcLZEa/GA2OIHWL+5F6js9\n-----END PRIVATE KEY-----\n",
#   "client_email": "orchard@orchard-390906.iam.gserviceaccount.com",
#   "client_id": "106478051947489167298",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/orchard%40orchard-390906.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }