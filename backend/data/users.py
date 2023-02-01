import mongoengine

class User (mongoengine.Document):
    user_id:mongoengine.ObjectIdField()
    registered_date:mongoengine.DateTimeField(default=datetime.datetime.now)
    name:mongoengine.StringField(required=True)
    username:mongoengine.StringField(required=True)
    email:mongoengine.StringField
    phone: ongoengine.NumericField(required=True)
    if_willing_to_share_location:mongoengine.BooleanField

    events = mongoengine.ListField()

meta = {
    'db_alias':'core,
    'coollection':'users'
}