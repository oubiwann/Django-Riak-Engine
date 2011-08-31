=====
Usage
=====

Setting up Django
-----------------

Let's get started with a demo app::

  $ django-admin.py startproject riakproj
  $ cd riakproj
  $ django-admin.py startapp riakapp

Configure the app to talk to a specific database in settings.py::

    DATABASES = {
        'default': {
            'ENGINE': 'django_riak_engine.riak',
            'NAME': 'mydatabase',
            'USER': '',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '8091',
            'SUPPORTS_TRANSACTIONS': False,
			'RIAK_TRANSPORT_CLASS':'riak.RiakHttpTransport', 
        },
    }


* riak.transports.pbc.RiakPbcCachedTransport A cache that reuses a set of protocol buffer connections. You can set a boundary of connections kept in the cache by specifying a maxsize attribute when creating the object.
* riak.transports.http.RiakHttpReuseTransport This transport is more efficient when reusing HTTP connections by setting SO_REUSEADDR on the underlying TCP socket. That allows the TCP stack to reuse connections before the TIME_WAIT state has passed.
* riak.transports.http.RiakHttpPoolTransport Use the urllib3 connection pool to pool connections to the same host. 


Using the Database
------------------

Let's created a model::

    from django.db import models

    class Article(models.Model):
        title = models.CharField(max_length = 64)
        content = models.TextField()


And a quick view that exercises it::

    from django.http import HttpResponse
    from models import *

    def testview(request):
      article = Article(title = 'test title',
        content = 'test content')
      article.save()

      return HttpResponse("<h1>Saved!</h1>")

Now let's use the Django Riak API::

    db.riakapp_article.find()

To get a list of all articles::

    articles = Article.objects.all()


