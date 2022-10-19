from libs.uow import BaseModel
from peewee import *

class Scheduler(BaseModel):
    name = CharField(null=True)
    description = TextField(null=True)
    date = DateTimeField(null=True)
    cron = CharField(null=True)
    status = IntegerField(null=True)

class Vault(BaseModel):
    name = CharField(null=True)
    secret =CharField(null=True)
