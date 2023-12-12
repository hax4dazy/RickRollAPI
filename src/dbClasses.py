from peewee import *

db = SqliteDatabase("database.db", pragmas={"foreign_keys": 1})

class BaseModel(Model):
    class Meta:
        database = db

class stats(BaseModel):
    name = CharField(default=0)
    count = IntegerField(default=0)


class isTheDatabaseSetup(BaseModel):
    isSetup = BooleanField(default=False)
