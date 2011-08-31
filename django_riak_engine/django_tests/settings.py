DATABASES = {
        'default': {
            'ENGINE': 'django_riak_engine.riak',
            'NAME': 'mydatabase',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '8098',
            'SUPPORTS_TRANSACTIONS': False, 
            'RIAK_TRANSPORT_CLASS':'riak.RiakHttpTransport', 
        },
}

# FIXME: Values  for transport: RiakPbcTransport, RiakPbcCachedTransport
# RiakHttpTransport, RiakHttpPoolTransport, RiakHttpReuseTransport
INSTALLED_APPS = ['djangotoolbox',]

LOGGING = {
    'version' : 1,
    'formatters' : {'simple' : {'format': '%(levelname)s %(message)s'}},
    'handlers' : {
        'console' : {
            'level' : 'DEBUG',
            'class' : 'logging.StreamHandler',
            'formatter' : 'simple'
        }
    },
    'loggers' : {
        'django.db.backends' : {
            'level' : 'DEBUG',
            'handlers' : ['console']
        }
    }
}  