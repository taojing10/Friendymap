class User(mongoengine.Document):
    ID = mongoengine.ObjectField
    username = mongoengine.StringField(required=True)
    Password = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    If_willing_to_share_location = mongoengine.BooleanField()
    create_time = mongoengine.DateTimeField(default=datetime.datetime.now)
    lasttime_updated = mongoengine.DateTimeField(default=datetime.datetime.now)
    Event = mongoengine.EmbededDocumentListField(Event)

    meta = {
        'db_alias': 'core',
        'collection': 'user'
    }

class Event(mongoengine.Document):
    ID = mongoengine.ObjectField
    event_name = mongoengine.StringField(required=True)
    event_start_Date = mongoengine.DateTimeField
    event_end_Date = mongoengine.DateTimeField
    hostID = mongoengine.ObjectField
    country = mongoengine.StringField
    state = mongoengine.StringField
    city = mongoengine.StringField
    street_address =mongoengine.StringField
    location = mongoengine。DictField
    event_discription = mongoengine.StringField
    create_time = mongoengine.DateTimeField(default=datetime.datetime.now)
    lasttime_updated = mongoengine.DateTimeField(default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'event'
    }
