"""
Django settings for tp_web_hw_instagram project.

Generated by "django-admin startproject" using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "-36+!f&$%t@@u@c6qu^-4^uizyzz#yk3#80*yb6mvty=l_#n-n"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "django_filters",

    "oauth2_provider",
    "social_django",
    "rest_framework_social_oauth2",

    "images",
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

ROOT_URLCONF = "tp_web_hw_instagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "tp_web_hw_instagram.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

MEDIA_ROOT = "media"
MEDIA_URL = "/media/"

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",  # django-oauth-toolkit >= 1.0.0
        "rest_framework_social_oauth2.authentication.SocialAuthentication",

    ],
}

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    "social_core.backends.facebook.FacebookAppOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",

    # django-rest-framework-social-oauth2
    "rest_framework_social_oauth2.backends.DjangoOAuth2",

    # Django
    "django.contrib.auth.backends.ModelBackend",
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "social_django.context_processors.backends",
    "social_django.context_processors.login_redirect",
)

SOCIAL_AUTH_FACEBOOK_KEY = "1181795715344708"
SOCIAL_AUTH_FACEBOOK_SECRET = "4bfa3eaa57553fb525b8b2942f24998d"

SOCIAL_AUTH_FACEBOOK_SCOPE = ["email"]
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    "fields": "id, name, email"
}

AUTH_USER_MODEL = "images.Creator"
