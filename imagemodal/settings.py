"""
Stub settings for xblock
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
    'imagemodal/translations',
]
SECRET_KEY = 'SECRET_KEY'
