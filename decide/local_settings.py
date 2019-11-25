ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://127.0.0.1:8000',
    'base': 'http://127.0.0.1:8000',
    'booth': 'http://127.0.0.1:8000',
    'census': 'http://127.0.0.1:8000',
    'mixnet': 'http://127.0.0.1:8000',
    'postproc': 'http://127.0.0.1:8000',
    'store': 'http://decide-test12.herokuapp.com',
    'visualizer': 'http://decide-test12.herokuapp.com',
    'voting': 'http://decide-test12.herokuapp.com',
}

BASEURL = 'http://decide-test12.herokuapp.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'decide',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'PASSWORD': 'decide',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
