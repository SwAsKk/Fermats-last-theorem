"""
Django settings for courseWork project.
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u)0^dr%*x!dlkg+x112ihh!1hwy$j#80osb=8e3bz9eg(wyetf"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "baton",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "baton.autodiscover",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Whitenoise static serve
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "courseWork.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "courseWork.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

# I18N, L10N, TZ for Moscow
LANGUAGE_CODE = "ru-RU"
TIME_ZONE = "Etc/GMT-3"

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Whitenoise serve settings
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"


BATON = {
    "SITE_HEADER": "Fermats",
    "SITE_TITLE": "FLT",
    "INDEX_TITLE": "Администрирование",
    "SUPPORT_HREF": "https://github.com/swaskk/fermats-last-theorem/",
    "COPYRIGHT": 'copyright © 2023 <a href="https://github.com/swaskk/">Leo Sobolev</a>',  # noqa
    "POWERED_BY": '<a href="https://github.com/swaskk/">Leo Sobolev</a>',
    "CONFIRM_UNSAVED_CHANGES": True,
    "SHOW_MULTIPART_UPLOADING": True,
    "ENABLE_IMAGES_PREVIEW": True,
    "CHANGELIST_FILTERS_IN_MODAL": True,
    "CHANGELIST_FILTERS_ALWAYS_OPEN": False,
    "CHANGELIST_FILTERS_FORM": True,
    "COLLAPSABLE_USER_AREA": False,
    "MENU_ALWAYS_COLLAPSED": False,
    "MENU_TITLE": "Меню",
    "MESSAGES_TOASTS": False,
    "GRAVATAR_DEFAULT_IMG": "retro",
    "GRAVATAR_ENABLED": True,
    "LOGIN_SPLASH": "/static/core/img/login-splash.png",
    "SEARCH_FIELD": {
        "label": "Поиск...",
        "url": "/search/",
    },
    # 'MENU': (
    #     { 'type': 'title', 'label': 'main', 'apps': ('auth', ) },
    #     {
    #         'type': 'app',
    #         'name': 'auth',
    #         'label': 'Authentication',
    #         'icon': 'fa fa-lock',
    #         'default_open': True,
    #         'models': (
    #             {
    #                 'name': 'user',
    #                 'label': 'Users'
    #             },
    #             {
    #                 'name': 'group',
    #                 'label': 'Groups'
    #             },
    #         )
    #     },
    #     { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
    #     { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
    #     { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
    #     { 'type': 'free', 'label': 'My parent voice', 'children': [
    #         { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp', 'icon': 'fa fa-gavel' },
    #         { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
    #     ] },
    # ),
    "ANALYTICS": None,
}
