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
    'authentication': 'http://decide-dialga-postproc.herokuapp.com',
    'base': 'http://decide-dialga-postproc.herokuapp.com',
    'booth': 'http://decide-dialga-postproc.herokuapp.com',
    'census': 'http://decide-dialga-postproc.herokuapp.com',
    'mixnet': 'http://decide-dialga-postproc.herokuapp.com',
    'postproc': 'http://decide-dialga-postproc.herokuapp.com',
    'store': 'http://decide-dialga-postproc.herokuapp.com',
    'visualizer': 'http://decide-dialga-postproc.herokuapp.com',
    'voting': 'http://decide-dialga-postproc.herokuapp.com',
}

BASEURL = 'http://decide-dialga-postproc.herokuapp.com'

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
