from django.core.exceptions import ImproperlyConfigured
from django.db.backends.signals import connection_created
from django.conf import settings
import riak

from djangotoolbox.db.base import NonrelDatabaseFeatures, \
    NonrelDatabaseOperations, NonrelDatabaseWrapper, NonrelDatabaseClient, \
    NonrelDatabaseValidation, NonrelDatabaseIntrospection, \
    NonrelDatabaseCreation

# TODO: You can either use the type mapping defined in NonrelDatabaseCreation
# or you can override the mapping, here:
class DatabaseCreation(NonrelDatabaseCreation):
    pass

class DatabaseFeatures(NonrelDatabaseFeatures):
    string_based_auto_field = True
    supports_dicts = True 

class DatabaseOperations(NonrelDatabaseOperations):
    compiler_module = __name__.rsplit('.', 1)[0] + '.compiler'

class DatabaseClient(NonrelDatabaseClient):
    pass

class DatabaseValidation(NonrelDatabaseValidation):
    pass

class DatabaseIntrospection(NonrelDatabaseIntrospection):
    pass

def requires_connection(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self._connected:
            self._connect()
        return method(self, *args, **kwargs)
    return wrapper 
    
class DatabaseWrapper(NonrelDatabaseWrapper):
    def __init__(self, *args, **kwds):
        super(DatabaseWrapper, self).__init__(*args, **kwds)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.client = DatabaseClient(self)
        self.creation = DatabaseCreation(self)
        self.validation = DatabaseValidation(self)
        self.introspection = DatabaseIntrospection(self)
        self._connected = False 
        def _connect(self):
            host = self.settings_dict['HOST'] or None
            port = self.settings_dict.get('PORT', None) 
            options = {
            'RIAK_TRANSPORT_CLASS': riak.RiakHttpTransport,
            }
            options.update(self.settings_dict.get('OPTIONS', {}))

                
            transport_class = options['RIAK_TRANSPORT_CLASS']
        return  
            self._connection = riak.RiakClient(host=host, port=port,transport_class=transport_class))
            self.db = self._connection[self.db_name]
            self._connected = True
            connection_created.send(sender=self.__class__, connection=self)
                
