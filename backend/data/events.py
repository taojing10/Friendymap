import mongoengine
import datetime

class Event (mongoengine.Document):
    event_id:mongoengine.ObjectIdField()
    registered_date:mongoengine.DateTimeField(default=datetime.datetime.now)
    event_name:mongoengine.StringField(required=True)
    event_start_date:mongoengine.DateTimeField
    event_end_date:mongoengine.DateTimeField
    host_user_name:mongoengine.StringField(required=True)
    username:mongoengine.StringField(required=True)
    email:mongoengine.StringField 
    if_willing_to_share_location:mongoengine.BooleanField(required=True)

meta = {
    'db_alias':'core,
    'coollection':'events'
}

