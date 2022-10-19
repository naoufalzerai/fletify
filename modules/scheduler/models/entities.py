from libs.uow import BaseModel
from peewee import *

class Scheduler(BaseModel):
    name = CharField()
    description = TextField()
    date = DateTimeField()
    cron = CharField()
    status = IntegerField()

class Vault(BaseModel):
    name = CharField()
    secret =CharField()
