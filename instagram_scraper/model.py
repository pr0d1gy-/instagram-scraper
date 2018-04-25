from pymodm import connect, fields, MongoModel

from . constants import (
    MONGODB_HOST,
    MONGODB_PORT,
    MONGODB_DB,
    MONGODB_URI,
    USERS_TABLE_NAME
)


connect(MONGODB_URI if MONGODB_URI else 'mongodb://{}:{}/{}'.format(
    MONGODB_HOST, MONGODB_PORT, MONGODB_DB
))


class UserModel(MongoModel):

    user_name = fields.CharField()
    user_dob = fields.CharField(blank=True)
    user_gender = fields.CharField(blank=True)
    user_location = fields.CharField(blank=True)
    folder_s3_url = fields.CharField()

    photos_count = fields.IntegerField(default=0)
    profile_unique_id = fields.CharField()
    spider_name = fields.CharField()

    indexed = fields.BooleanField(default=False)
    clustered = fields.BooleanField(default=False)
    verified = fields.BooleanField(default=False)

    class Meta:

        final = True
        collection_name = USERS_TABLE_NAME
