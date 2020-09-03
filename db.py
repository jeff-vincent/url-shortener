from peewee import *

db = SqliteDatabase('urls.db')

class URLMapping(Model):
    url_hash = CharField()
    url = CharField()

    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([URLMapping], safe=True)
    db.close()

initialize_db()