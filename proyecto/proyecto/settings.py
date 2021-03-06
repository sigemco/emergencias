"""
Django settings for proyecto project.

Generated by 'django-admin startproject' using Django 2.2.4.

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
SECRET_KEY = 'svgiw=kkkila#z3=xp^2!fd0@o#u0pvi6(d7k3(@#inb((cs%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.150.1', 'sigemcomae.sytes.net']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'crispy_forms',
    'widget_tweaks',
    'core',
    'leaflet',
    # necesario delcarar la aplicacion asi como sigue para q reconozca signals.py
    'emergencias.apps.EmergenciasConfig',
    'bootstrap4',
    'guardian',
    'groups_manager',
    'easy_thumbnails',
    'filer',
    'mptt',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)


# Configuracion para channels
# https://www.digitalocean.com/community/tutorials/como-instalar-y-proteger-redis-en-ubuntu-18-04-es
ASGI_APPLICATION = "proyecto.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates/')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media', #https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': 'emergencias',
        'NAME': 'emergenciasdb',
       'PASSWORD':'emergencias',
      'HOST':'localhost',
      'PORT':'5433'
    },
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-AR'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/home/sigemco/statics')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

#https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/index/'

LOGOUT_REDIRECT_URL = '/'

AUTH_USER_MODEL = 'core.UserSigemco'

LEAFLET_CONFIG = {
'DEFAULT_CENTER': (-40.66,-58.72),
'DEFAULT_ZOOM': 4,
'MIN_ZOOM': 3,
'MAX_ZOOM': 18,
'TILES': [('OSM','http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{'attribution': '&copy; Big eye', 'maxZoom': 16}),
          ('Rutas','https://{s}.google.com/vt/lyrs=m@221097413,traffic&x={x}&y={y}&z={z}', { 'maxZoom': 20,'minZoom': 2,
                            'subdomains': ['mt0', 'mt1', 'mt2', 'mt3'],
    }),('Relieve','http://{s}.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',{
    'maxZoom': 20,
    'subdomains':['mt0','mt1','mt2','mt3']}),
    ('Hibrido','http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
    'maxZoom': 20,
    'subdomains':['mt0','mt1','mt2','mt3']
}),
    ('Argis', 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
        'attribution': '&copy',
        'maxZoom': 18,
        }),('Argenmap','https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{y}.png', {
		    'tms': 'true',
		    'maxZoom': 21,
		    'attribution': 'atrib_ign'
			}),],

'OVERLAYS': [],
'PLUGINS': {
'leafletCSV': {
        'js': 'app/lib/leaflet/leaflet.geocsv.js',
        'auto-include': True,
    },
'cartodb': {
        'js': 'app/lib/leaflet/L.CartoDB.js',
        'auto-include': True,
    },


}


}
