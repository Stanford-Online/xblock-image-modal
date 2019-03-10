"""
Stub Settings for imagemodal xblock
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'intentionally-omitted',
    },
}
INSTALLED_APPS = (
    'imagemodal',
)
LOCALE_PATHS = [
    'imagemodal/locale',
]
SECRET_KEY = 'SECRET_KEY'
