#registering connection.

#step1 import mongoengine
import mongoengine

#set up 'alias' and 'name'
def global_init():
    mongoengine.register_connection(alias='core',name='Friendymap_db')
