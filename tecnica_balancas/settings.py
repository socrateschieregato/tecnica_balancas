import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['https://tecnica-balancas.herokuapp.com/']

INSTALLED_APPS = [
    # 'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'home',
    'tabelas',
    'empresas',
    'api',
    'calibracoes',
    'equipamentos'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tecnica_balancas.urls'

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

WSGI_APPLICATION = 'tecnica_balancas.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFUALT_PERMISSION_CLASSES': {
        'rest_framework.permissions.IsAuthenticated'
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # noqa
    },
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static/',
]

LOGIN_REDIRECT_URL = 'home'

# # Django Suit configuration example
# SUIT_CONFIG = {
#     # header
#     'ADMIN_NAME': 'Técnica Balanças',
#     'HEADER_DATE_FORMAT': 'l, j, F Y',
#     'HEADER_TIME_FORMAT': 'H:i',
#
#     # forms
#     'SHOW_REQUIRED_ASTERISK': True,  # Default True
#     'CONFIRM_UNSAVED_CHANGES': True, # Default True
#
#     # menu
#     'SEARCH_URL': '/admin/auth/user/',
#     'MENU_ICONS': {
#        'sites': 'icon-leaf',
#        'auth': 'icon-lock',
#     },
#     'MENU_OPEN_FIRST_CHILD': True, # Default True
#     'MENU_EXCLUDE': ('auth.group',),
#     'MENU': (
#         'sites',
#         {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
#         {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
#         {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
#     ),
#
#     # misc
#     'LIST_PER_PAGE': 15
# }

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]