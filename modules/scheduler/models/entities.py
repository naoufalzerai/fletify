from libs.uow import BaseModel
from peewee import *

class Scheduler(BaseModel):
    name = CharField()
    date = CharField()
    cron = CharField()

class Vault(BaseModel):
    name = CharField()
    secret =CharField()
