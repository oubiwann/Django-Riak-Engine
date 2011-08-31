from django.test import TestCase
from django.conf import settings
from django.db import connections
from riak.test_server import TestServer  

RIAK_PATH="/usr/local/bin/"

class TestCase(TestCase):
    """
    This should enable DEBUG and start riak test server 
    server = TestServer(bin_dir="/usr/local/riak/0.14.2/bin")
    You can also overwrite the default settings used to generate the app.config file for the in-memory Riak instance. Just specify a keyword pointing to a dictionary for every section in the app.config like so:
    server = TestServer(riak_core={"web_port": 8080})  
    """
    def setUp(self):
        super(TestCase, self).setUp()
        if getattr(settings, 'TEST_DEBUG', False):
            settings.DEBUG = True
        self.testserver = TestServer(bin_dir=RIAK_PATH)
        self.testserver.prepare()
        self.testserver.start()
    def tearDown(self):
        self.server.recycle()
        

def skip_all_except(*tests):
    class meta(type):
        def __new__(cls, name, bases, dict):
            for attr in dict.keys():
                if attr.startswith('test_') and attr not in tests:
                    del dict[attr]
            return type.__new__(cls, name, bases, dict)
    return meta

def get_bucket(model):
    return connections['default'].get_bucket(model._meta.db_table)      